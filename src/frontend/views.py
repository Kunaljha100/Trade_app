import datetime
from django.shortcuts import render
from django.http import HttpResponse
import requests
from django.contrib import messages
from trading_component.models import order
from .form import (
    OrderModelForm,
    LoginForm,
    CustomUserCreationForm,
    User,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, reverse, redirect
import time
from django.views import generic
from django.contrib.auth import login, authenticate  # add to imports
import json
# Create your views here.


def get_header():
    header = {
        "Content-Type": "application/json",
        "X-Client-Id": "6786787678f7dd8we77e787",
        "X-Client-Secret": "96777676767585",
    }
    return header


class SignupView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse("login")


def login_page(request):

    form_class = LoginForm

    message = ''
    form = LoginForm
    if request.method == 'POST':
        form = form_class(request.POST)

        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                message = 'Hello {user.username}! You have been logged in'
                return redirect("/")
            else:
                message = 'Login failed!'
    return render(request,
                  'registration/login.html',
                  context={
                      'message': message,
                      'form': form
                  })


@login_required
def index(request):
    response = requests.get('http://127.0.0.1:8000/api',
                            params=request.GET).json()
    return render(request, 'orders/order_list.html', {'response': response})


def home(request):
    response = order.objects.all()

    print("Response :", response)
    return render(request, 'books/book_list_student.html',
                  {'response': response})


def orderview(request):
    if request.method == 'POST':
        r = requests.post('http://127.0.0.1:8000/api', params=request.POST)
    else:
        r = requests.get('http://127.0.0.1:8000/api',
                         params=request.GET).json()
    return render(request, 'orders/order_list.html', {'response': r})


def create_view(request):
    r = ''
    entry_price = request.POST.get('entry_price')
    quantity = request.POST.get('quantity')
    trade_type = request.POST.get('trade_type')
    # entery_price = request.POST['entery_price']
    payload = {
        'entry_price': (entry_price),
        'quantity': (quantity),
        'trade_type': trade_type,
        'user': request.user.id
    }

    if request.method == 'POST':

        result = requests.post('http://127.0.0.1:8000/api',
                               data=json.dumps(payload),
                               headers=get_header())
        return redirect("/")

    return render(request, 'orders/order_create.html', {'response': r})


def order_detail(request, pk):
    order = order.objects.get(id=pk)
    context = {"order": order}
    return render(request, "orders/order_detail.html", context)


def update_view(request, pk):
    context = {}
    order_data = order.objects.get(id=pk)
    form = OrderModelForm(request.POST or None, instance=order_data)

    if form.is_valid():
        form.save()
        messages.info(request, "You have successfully updated order")
        return redirect("/")
    context["form"] = form

    return render(request, "order/order_update.html", context)


def delete_view(request, pk):
    context = {}
    order_data = order.objects.get(id=pk)

    if request.method == "POST":

        order_data.delete()

        messages.info(request, "You have successfully deleted order")
        return redirect("/")

    return render(request, "orders/order_delete.html", context)

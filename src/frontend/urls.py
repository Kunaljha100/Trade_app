from django.urls import path
from .views import index,login_page,order_detail,orderview,create_view,update_view,delete_view,SignupView,home
from django.contrib.auth.views import (
    
    LogoutView, 
    PasswordResetView, 
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
    
   
    
)

urlpatterns = [
   
    path('',index,name="home"),
    path('login/', login_page, name='login'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('<int:pk>/', order_detail, name='book_detail'),
    path('order/', orderview, name='order_view'),
    path('create/', create_view, name='create_order'),
    path('update/<int:pk>', update_view, name='update_book'),
    path('delete/<int:pk>', delete_view, name='delete_book'),
    path('reset-password/', PasswordResetView.as_view(), name='reset-password'),
    path('password-reset-done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset-complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
   
]

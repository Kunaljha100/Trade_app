from django.urls import path
from .views import orderView,OrderRetrieveView,OrderDetailUpdateView,OrderDetailDeleteView

urlpatterns = [
    path('',orderView.as_view(),name="add_order"),
    path('get-detail/<int:pk>', OrderRetrieveView.as_view(), name="get_detail"),
    path('update-detail/<int:pk>', OrderDetailUpdateView.as_view(), name="update_detail"),
     path('delete-detail/<int:pk>', OrderDetailDeleteView.as_view(), name="delete"),
    
   
]

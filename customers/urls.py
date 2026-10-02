from django.urls import path

from . import views

urlpatterns = [
    path('', views.list_create_customers, name='customer_list_create'),
    path('<int:pk>/', views.retrieve_update_delete_customer, name='customer_detail'),
]

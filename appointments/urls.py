from django.urls import path

from . import views

urlpatterns = [
    path('services/', views.list_create_services, name='service_list_create'),
    path('', views.list_create_appointments, name='appointment_list_create'),
    path('<int:pk>/', views.retrieve_update_delete_appointment, name='appointment_detail'),
]

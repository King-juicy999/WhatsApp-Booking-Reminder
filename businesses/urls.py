from django.urls import path

from . import views

urlpatterns = [
    path('', views.list_create_businesses, name='business_list_create'),
    path('<int:pk>/', views.retrieve_update_delete_business, name='business_detail'),
]

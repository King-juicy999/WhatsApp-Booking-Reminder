from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/businesses/', include('businesses.urls')),
    path('api/customers/', include('customers.urls')),
    path('api/appointments/', include('appointments.urls')),
]

from django.contrib import admin

from .models import Appointment, Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'business', 'duration_minutes', 'price')
    list_filter = ('business',)
    search_fields = ('name',)


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('customer', 'service', 'start_time', 'status', 'created_at')
    list_filter = ('status', 'service__business')
    search_fields = ('customer__name', 'customer__phone_number')
    list_select_related = ('customer', 'service')

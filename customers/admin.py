from django.contrib import admin

from .models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'business', 'created_at')
    list_filter = ('business',)
    search_fields = ('name', 'phone_number')

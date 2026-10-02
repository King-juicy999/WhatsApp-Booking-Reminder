from django.contrib import admin

from .models import Business


@admin.register(Business)
class BusinessAdmin(admin.ModelAdmin):
    list_display = ('name', 'whatsapp_number', 'timezone', 'created_at')
    search_fields = ('name', 'whatsapp_number')

from django.contrib import admin

from .models import Reminder


@admin.register(Reminder)
class ReminderAdmin(admin.ModelAdmin):
    list_display = ('appointment', 'reminder_time', 'sent_status', 'created_at')
    list_filter = ('sent_status',)
    list_select_related = ('appointment__customer', 'appointment__service')

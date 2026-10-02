from django.db import models

from appointments.models import Appointment


class Reminder(models.Model):
    appointment = models.ForeignKey(
        Appointment,
        on_delete=models.CASCADE,
        related_name='reminders',
    )
    reminder_time = models.DateTimeField()
    sent_status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Reminder for {self.appointment} at {self.reminder_time}'

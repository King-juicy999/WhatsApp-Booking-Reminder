from django.db import models


class Business(models.Model):
    name = models.CharField(max_length=255)
    whatsapp_number = models.CharField(max_length=20, unique=True)
    timezone = models.CharField(max_length=50, default='UTC')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

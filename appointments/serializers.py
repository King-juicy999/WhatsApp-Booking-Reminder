from rest_framework import serializers

from .models import Appointment, Service


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = (
            'id',
            'business',
            'name',
            'duration_minutes',
            'price',
        )
        read_only_fields = ('id',)


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = (
            'id',
            'customer',
            'service',
            'start_time',
            'status',
            'created_at',
        )
        read_only_fields = ('id', 'created_at')

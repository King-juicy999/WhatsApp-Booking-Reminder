from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Appointment, Service
from .serializers import AppointmentSerializer, ServiceSerializer


@api_view(['GET', 'POST'])
def list_create_services(request):
    if request.method == 'GET':
        serializer = ServiceSerializer(Service.objects.all(), many=True)
        return Response(serializer.data)

    serializer = ServiceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def retrieve_update_delete_service(request, pk):
    try:
        service = Service.objects.get(pk=pk)
    except Service.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return Response(ServiceSerializer(service).data)

    if request.method == 'DELETE':
        service.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    serializer = ServiceSerializer(
        service,
        data=request.data,
        partial=request.method == 'PATCH',
    )
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def list_create_appointments(request):
    if request.method == 'GET':
        serializer = AppointmentSerializer(Appointment.objects.all(), many=True)
        return Response(serializer.data)

    serializer = AppointmentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def retrieve_update_delete_appointment(request, pk):
    try:
        appointment = Appointment.objects.get(pk=pk)
    except Appointment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return Response(AppointmentSerializer(appointment).data)

    if request.method == 'DELETE':
        appointment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    serializer = AppointmentSerializer(
        appointment,
        data=request.data,
        partial=request.method == 'PATCH',
    )
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

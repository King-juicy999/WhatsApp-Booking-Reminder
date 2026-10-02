from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Business
from .serializers import BusinessSerializer


@api_view(['GET', 'POST'])
def list_create_businesses(request):
    if request.method == 'GET':
        serializer = BusinessSerializer(Business.objects.all(), many=True)
        return Response(serializer.data)

    serializer = BusinessSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def retrieve_update_delete_business(request, pk):
    try:
        business = Business.objects.get(pk=pk)
    except Business.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return Response(BusinessSerializer(business).data)

    if request.method == 'DELETE':
        business.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    serializer = BusinessSerializer(
        business,
        data=request.data,
        partial=request.method == 'PATCH',
    )
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from typing import Dict, Any

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from devicedata.serializers import DeviceDataSerializer


@api_view(['GET', 'POST'])
def post_data(request):
    if request.method == 'POST':
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        device_id = request.query_params.get('d', None)
        ac_voltage = request.query_params.get('v', None)
        battery_charge = request.query_params.get('b', None)

        received_data: Dict[str, Any] = dict()

        received_data['device_id'] = device_id
        received_data['ac_voltage'] = ac_voltage
        received_data['battery_charge'] = battery_charge

        serializer = DeviceDataSerializer(data=received_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response(status=status.HTTP_400_BAD_REQUEST)

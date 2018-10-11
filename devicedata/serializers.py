from rest_framework import serializers
from .models import DeviceData



class DeviceDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceData
        fields = ('device_id', 'ac_voltage', 'battery_charge')
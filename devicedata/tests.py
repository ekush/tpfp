from django.test import TestCase
from .models import DeviceData

# Create your tests here.

class DatabaseTest(TestCase):

    def setUp(self):
        DeviceData.objects.create(device_id='device1', ac_voltage = '50', battery_charge = '30')
        DeviceData.objects.create(device_id='device2', ac_voltage = '60', battery_charge = '70')
        DeviceData.objects.create(device_id='device3', ac_voltage = '90', battery_charge = '100')

    def test_device_data_entry_successful(self):
        device1 = DeviceData.objects.get(device_id='device1')
        device2 = DeviceData.objects.get(device_id='device2')
        device3 = DeviceData.objects.get(device_id='device3')

        self.assertEqual(device1.battery_charge, '30')
        self.assertEqual(device2.battery_charge, '70')
        self.assertEqual(device3.battery_charge, '100')

class DataPostAndGetTest(TestCase):
    pass
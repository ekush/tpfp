from .models import *


def populate_device_profile(device_tag, device_long, device_lat):
    device_prifle = DeviceProfile.objects.create(device_tag=device_tag, device_long=device_long, device_lat=device_lat)
    device_prifle.save()


def populate_device_data():
    pass
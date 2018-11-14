from django.db import models

# Create your models here.

class DeviceProfile(models.Model):
    device_tag = models.CharField("Tag", max_length=50, blank=True, null=True)



class DeviceData(models.Model):
    date = models.DateField("Date", auto_now_add=True)
    time = models.TimeField("Time", auto_now_add=True)
    device_id = models.CharField("Device ID", max_length=50, null=True, blank=True)
    ac_voltage = models.CharField("AC Voltage", max_length=50, null=True, blank=True)
    battery_charge = models.CharField("Battery Charge", max_length=50, null=True, blank=True)
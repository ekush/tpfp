from django.db import models


class DeviceProfile(models.Model):
    device_tag = models.CharField("Tag", max_length=50, blank=True, null=True)


class DeviceData(models.Model):
    date = models.DateField("Date", auto_now_add=True)
    time = models.TimeField("Time", auto_now_add=True)
    device_id = models.IntegerField("Device ID", null=True, blank=True)
    ac_voltage = models.IntegerField("AC Voltage", null=True, blank=True)
    battery_charge = models.IntegerField("Battery Charge", null=True, blank=True)


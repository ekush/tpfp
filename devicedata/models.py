from django.db import models


class DeviceProfile(models.Model):
    device_tag = models.CharField("Tag", max_length=50, blank=True, null=True)
    device_long = models.DecimalField("Long", max_digits=9, decimal_places=6)
    device_lat = models.DecimalField("Lat", max_digits=9, decimal_places=6)
    device_installation_date = models.DateField("Installation Date",  auto_now_add=True)

    def __str__(self):
        return self.pk


class DeviceData(models.Model):
    date = models.DateField("Date", auto_now_add=True)
    time = models.TimeField("Time", auto_now_add=True)
    device_id = models.ForeignKey(DeviceProfile, null=True, blank=True, on_delete=models.CASCADE)
    ac_voltage = models.IntegerField("AC Voltage", null=True, blank=True)
    battery_charge = models.IntegerField("Battery Charge", null=True, blank=True)


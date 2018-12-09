from django.contrib import admin
from .models import DeviceData, DeviceProfile


# Register your models here.

@admin.register(DeviceProfile)
class DeviceProfileAdmin(admin.ModelAdmin):
    list_display = [f.name for f in DeviceProfile._meta.fields]


@admin.register(DeviceData)
class DeviceDataAdmin(admin.ModelAdmin):
    list_display = [f.name for f in DeviceData._meta.fields]

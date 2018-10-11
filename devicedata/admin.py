from django.contrib import admin
from .models import DeviceData

# Register your models here.

@admin.register(DeviceData)
class DeviceDataAdmin(admin.ModelAdmin):
    list_display = [f.name for f in DeviceData._meta.fields]

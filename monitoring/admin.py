from django.contrib import admin
from .models import School, AirQualityReading


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'latitude', 'longitude']
    search_fields = ['name', 'location']


@admin.register(AirQualityReading)
class AirQualityReadingAdmin(admin.ModelAdmin):
    list_display = ['school', 'pollutant', 'value', 'measured_at']
    list_filter = ['pollutant', 'measured_at']
    search_fields = ['school__name']
    date_hierarchy = 'measured_at'

# Register your models here.

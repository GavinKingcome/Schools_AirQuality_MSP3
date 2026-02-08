from django.db import models
from django.contrib.auth.models import User

class School(models.Model):
    """A school that we're monitoring - US-1"""
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    latitude = models.FloatField()
    longitude = models.FloatField()
    
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='schools')
    
    def get_latest_reading(self, pollutant="PM2.5"):
        """Get most recent pollution reading for a specific pollutant"""
        latest = self.readings.filter(  # ← CHANGED from airqualityreading_set
            pollutant=pollutant
        ).first()
        return latest.value if latest else None
    
    def get_average_reading(self, pollutant="PM2.5"):
        """Calculate average pollution over all time (historical + current)"""
        from django.db.models import Avg
        avg = self.readings.filter(  # ← CHANGED
            pollutant=pollutant
        ).aggregate(Avg('value'))
        return avg['value__avg']
    
    def get_peak_reading(self, pollutant="PM2.5"):
        """Get highest pollution reading ever recorded - US-7"""
        from django.db.models import Max
        peak = self.readings.filter(  # ← CHANGED
            pollutant=pollutant
        ).aggregate(Max('value'))
        return peak['value__max']
    
    def get_peak_reading_detail(self, pollutant="PM2.5"):
        """Get full details of the highest reading (value + date) - US-7"""
        peak = self.readings.filter(  # ← CHANGED
            pollutant=pollutant
        ).order_by('-value').first()
        return peak
    
    def get_top_readings(self, pollutant="PM2.5", limit=5):
        """Get the top N highest readings ever recorded - US-7"""
        return self.readings.filter(  # ← CHANGED
            pollutant=pollutant
        ).order_by('-value')[:limit]
    
    def __str__(self):
        return f"{self.name} ({self.location})"


class AirQualityReading(models.Model):
    """A single pollution measurement - handles current and historical data - US-4"""
    
    POLLUTANT_CHOICES = [
        ('PM2.5', 'PM2.5 (Fine Particulate Matter)'),
        ('NO2', 'NO2 (Nitrogen Dioxide)'),
        ('PM10', 'PM10 (Coarse Particulate Matter)'),
        ('O3', 'O3 (Ozone)'),
        ('SO2', 'SO2 (Sulfur Dioxide)'),
    ]
    
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='readings')
    pollutant = models.CharField(max_length=50, choices=POLLUTANT_CHOICES)
    value = models.FloatField()
    measured_at = models.DateTimeField()
    
    def __str__(self):
        return f"{self.school.name} - {self.pollutant}: {self.value} on {self.measured_at.date()}"
    
    class Meta:
        ordering = ['-measured_at']
        verbose_name = "Air Quality Reading"
        verbose_name_plural = "Air Quality Readings"
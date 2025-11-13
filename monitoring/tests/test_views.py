from django.test import TestCase, Client
from django.urls import reverse
from monitoring.models import School, AirQualityReading
from datetime import datetime
from django.utils import timezone


class MapViewTest(TestCase):
    """Test the interactive map view - US-2"""
    
    def setUp(self):
        """Create test data before each test"""
        self.client = Client()
        
        # Create test school
        self.school = School.objects.create(
            name="Test School",
            location="London, UK",
            latitude=51.5074,
            longitude=-0.1278
        )
        
        # Create test pollution readings
        AirQualityReading.objects.create(
            school=self.school,
            pollutant='PM2.5',
            value=35.2,
            measured_at=timezone.now()
        )
        
        AirQualityReading.objects.create(
            school=self.school,
            pollutant='NO2',
            value=42.5,
            measured_at=timezone.now()
        )
    
    def test_map_view_loads(self):
        """Test that map view returns 200 OK - US-2"""
        response = self.client.get(reverse('home'))
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'monitoring/map.html')
    
    def test_map_view_contains_schools(self):
        """Test that map view includes school data - US-2"""
        response = self.client.get(reverse('home'))
        
        # Check school name appears
        self.assertContains(response, 'Test School')
        
        # Check coordinates appear (for Leaflet)
        self.assertContains(response, '51.5074')
        self.assertContains(response, '-0.1278')
    
    def test_map_view_includes_pollution_data(self):
        """Test that latest pollution readings are shown - US-2"""
        response = self.client.get(reverse('home'))
        
        # Check PM2.5 and NO2 values appear
        self.assertContains(response, '35.2')
        self.assertContains(response, '42.5')
    
    def test_map_view_with_no_schools(self):
        """Test map view when no schools exist - US-2"""
        School.objects.all().delete()
        
        response = self.client.get(reverse('home'))
        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No schools')
import requests
from django.core.management.base import BaseCommand
from django.utils import timezone
from monitoring.models import School, AirQualityReading
from datetime import datetime


def fetch_data_for_school(school):
    """
    Fetch air quality data for a single school from OpenAQ API - US-5
    
    Args:
        school: School object with latitude/longitude
        
    Returns:
        bool: True if successful, False if failed
    """
    try:
        # Build OpenAQ API URL
        url = "https://api.openaq.org/v2/measurements"
        params = {
            'coordinates': f'{school.latitude},{school.longitude}',
            'radius': 5000,  # 5km radius
            'parameter': 'pm25,no2',
            'limit': 100,
            'order_by': 'datetime',
            'sort': 'desc'
        }
        
        # Make API request
        response = requests.get(url, params=params, timeout=10)
        
        if response.status_code != 200:
            print(f"API returned status code {response.status_code}")
            return False
        
        # Parse JSON response
        data = response.json()
        results = data.get('results', [])
        
        if not results:
            print(f"No data found for {school.name}")
            return False
        
        # Store each measurement
        stored_count = 0
        for measurement in results:
            parameter = measurement.get('parameter')
            value = measurement.get('value')
            date_info = measurement.get('date', {})
            utc_string = date_info.get('utc')
            
            if not all([parameter, value, utc_string]):
                continue
            
            # Map API parameter names to our model
            pollutant_map = {
                'pm25': 'PM2.5',
                'no2': 'NO2'
            }
            pollutant = pollutant_map.get(parameter)
            
            if not pollutant:
                continue
            
            # Parse timestamp
            measured_at = datetime.fromisoformat(utc_string.replace('Z', '+00:00'))
            
            # Check for duplicates
            existing = AirQualityReading.objects.filter(
                school=school,
                pollutant=pollutant,
                measured_at=measured_at
            ).exists()
            
            if existing:
                continue
            
            # Create new reading
            AirQualityReading.objects.create(
                school=school,
                pollutant=pollutant,
                value=value,
                measured_at=measured_at
            )
            stored_count += 1
        
        print(f"✓ Stored {stored_count} reading(s) for {school.name}")
        return True
        
    except Exception as e:
        print(f"✗ Error fetching data for {school.name}: {str(e)}")
        return False


class Command(BaseCommand):
    """Django management command to fetch air quality data - US-5"""
    help = 'Fetch air quality data from OpenAQ API for all schools'
    
    def handle(self, *args, **options):
        schools = School.objects.all()
        
        if not schools.exists():
            self.stdout.write(self.style.WARNING('No schools found in database'))
            return
        
        self.stdout.write(f'Fetching air quality data for {schools.count()} school(s)...\n')
        
        success_count = 0
        fail_count = 0
        
        for school in schools:
            if fetch_data_for_school(school):
                success_count += 1
            else:
                fail_count += 1
        
        self.stdout.write(self.style.SUCCESS(
            f'\n✓ Successfully fetched data for {success_count}/{schools.count()} school(s)'
        ))
        
        if fail_count > 0:
            self.stdout.write(self.style.WARNING(
                f'✗ Failed to fetch data for {fail_count} school(s)'
            ))
import requests
import os
import time
from django.core.management.base import BaseCommand
from monitoring.models import School, AirQualityReading
from django.utils import timezone
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()


class Command(BaseCommand):
    help = 'Fetch air quality data from OpenAQ API v3'

    def handle(self, *args, **options):
        api_key = os.environ.get('OPEN_AQ_API_KEY')
        
        if not api_key:
            self.stdout.write(self.style.ERROR('❌ OPEN_AQ_API_KEY not found in .env file'))
            self.stdout.write('Get a free API key from: https://openaq.org/')
            return
        
        schools = School.objects.all()
        
        if not schools.exists():
            self.stdout.write(self.style.WARNING('No schools found in database'))
            return
            
        self.stdout.write(f"Fetching air quality data for {schools.count()} school(s)...\n")
        
        headers = {
            'Accept': 'application/json',
            'X-API-Key': api_key
        }
        
        # Cache sensor info to avoid repeated API calls
        sensor_cache = {}
        
        success_count = 0
        fail_count = 0
        
        for school in schools:
            time.sleep(1)  # Rate limiting
            
            try:
                # Step 1: Find nearby locations
                locations_url = "https://api.openaq.org/v3/locations"
                
                locations_params = {
                    'coordinates': f"{school.latitude},{school.longitude}",
                    'radius': 5000,  # 5km
                    'limit': 5
                }
                
                self.stdout.write(f"📍 {school.name}...")
                locations_response = requests.get(locations_url, params=locations_params, headers=headers, timeout=15)
                
                if locations_response.status_code != 200:
                    self.stdout.write(self.style.ERROR(f"   ✗ API error: {locations_response.status_code}\n"))
                    fail_count += 1
                    continue
                
                locations_data = locations_response.json()
                locations = locations_data.get('results', [])
                
                if not locations:
                    self.stdout.write(self.style.WARNING(f"   ⚠ No monitoring stations within 5km\n"))
                    fail_count += 1
                    continue
                
                # Step 2: Get latest measurements
                stored_count = 0
                
                location = locations[0]
                location_id = location.get('id')
                location_name = location.get('name', 'Unknown')
                
                self.stdout.write(f"   Using: {location_name}")
                
                latest_url = f"https://api.openaq.org/v3/locations/{location_id}/latest"
                
                time.sleep(0.5)
                latest_response = requests.get(latest_url, headers=headers, timeout=15)
                
                if latest_response.status_code == 200:
                    latest_data = latest_response.json()
                    measurements = latest_data.get('results', [])
                    
                    for measurement in measurements:
                        value = measurement.get('value')
                        sensors_id = measurement.get('sensorsId')
                        datetime_info = measurement.get('datetime', {})
                        timestamp_str = datetime_info.get('utc')
                        
                        if not sensors_id or value is None or not timestamp_str:
                            continue
                        
                        # Get sensor info (with caching)
                        if sensors_id not in sensor_cache:
                            time.sleep(0.3)
                            sensors_url = f"https://api.openaq.org/v3/sensors/{sensors_id}"
                            sensors_response = requests.get(sensors_url, headers=headers, timeout=10)
                            
                            if sensors_response.status_code == 200:
                                sensor_data = sensors_response.json()
                                
                                # Access results array first
                                sensor_results = sensor_data.get('results', [])
                                if sensor_results:
                                    sensor_info_obj = sensor_results[0]
                                    parameter_info = sensor_info_obj.get('parameter', {})
                                    
                                    parameter_id = parameter_info.get('id')
                                    parameter_name = parameter_info.get('name')
                                    
                                    sensor_cache[sensors_id] = {
                                        'id': parameter_id,
                                        'name': parameter_name
                                    }
                                    self.stdout.write(f"   Sensor {sensors_id}: {parameter_name} (ID: {parameter_id})")
                                else:
                                    sensor_cache[sensors_id] = None
                            else:
                                self.stdout.write(f"   ✗ Sensor {sensors_id} API error: {sensors_response.status_code}")
                                sensor_cache[sensors_id] = None
                        
                        sensor_info = sensor_cache.get(sensors_id)
                        if not sensor_info:
                            continue
                        
                        parameter_id = sensor_info.get('id')
                        
                        # Map to our pollutant names
                        pollutant_map = {
                            1: 'PM10',   # Fresh data available
                            2: 'PM2.5',  # Will be filtered if stale
                            5: 'NO2'     # Fresh data available
                        }
                        
                        pollutant = pollutant_map.get(parameter_id)
                        
                        if pollutant:
                            try:
                                measured_at = datetime.fromisoformat(timestamp_str.replace('Z', '+00:00'))
                            except:
                                measured_at = timezone.now()
                            
                            # Calculate age of reading
                            age_hours = (timezone.now() - measured_at).total_seconds() / 3600
                            
                            # Skip readings older than 7 days (168 hours)
                            if age_hours > 120:
                                self.stdout.write(f"   ⚠ Skipping stale {pollutant}: {value} µg/m³ ({age_hours:.0f}h / {age_hours/24:.1f} days old)")
                                continue
                            
                            # Store reading
                            reading, created = AirQualityReading.objects.get_or_create(
                                school=school,
                                pollutant=pollutant,
                                measured_at=measured_at,
                                defaults={'value': value}
                            )
                            
                            if created:
                                stored_count += 1
                                self.stdout.write(f"   ✓ {pollutant}: {value} µg/m³ ({age_hours:.1f}h old)")
                
                if stored_count > 0:
                    self.stdout.write(self.style.SUCCESS(f"   ✓ Stored {stored_count} new reading(s)\n"))
                    success_count += 1
                else:
                    self.stdout.write(self.style.WARNING(f"   ⚠ No fresh readings\n"))
                    success_count += 1
                    
            except requests.exceptions.Timeout:
                self.stdout.write(self.style.ERROR(f"   ✗ Timeout\n"))
                fail_count += 1
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"   ✗ Error: {str(e)}\n"))
                import traceback
                self.stdout.write(traceback.format_exc())
                fail_count += 1
        
        # Summary
        self.stdout.write("=" * 60)
        if success_count > 0:
            self.stdout.write(self.style.SUCCESS(f"✓ Successfully fetched data for {success_count}/{schools.count()} school(s)"))
        if fail_count > 0:
            self.stdout.write(self.style.ERROR(f"✗ Failed for {fail_count} school(s)"))
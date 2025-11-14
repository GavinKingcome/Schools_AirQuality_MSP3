from django.shortcuts import render
from django.http import JsonResponse
from .models import School, AirQualityReading
import json

def map_view(request):
    schools = School.objects.all()
    
    # DEBUG: Print school count
    print(f"DEBUG: Found {schools.count()} schools")
    
    schools_data = []
    for school in schools:
        # Get latest readings for PM10 and NO2
        pm10_reading = AirQualityReading.objects.filter(
            school=school,
            pollutant='PM10'
        ).order_by('-measured_at').first()
        
        no2_reading = AirQualityReading.objects.filter(
            school=school,
            pollutant='NO2'
        ).order_by('-measured_at').first()
        
        school_dict = {
            'name': school.name,
            'address': school.location,
            'latitude': school.latitude,
            'longitude': school.longitude,
            'readings': {
                'PM10': pm10_reading.value if pm10_reading else None,
                'NO2': no2_reading.value if no2_reading else None
            }
        }
        
        # DEBUG: Print each school
        print(f"DEBUG: Adding {school.name} at ({school.latitude}, {school.longitude})")
        
        schools_data.append(school_dict)
    
    # DEBUG: Print final JSON
    print(f"DEBUG: Total schools in JSON: {len(schools_data)}")
    print(f"DEBUG: JSON data: {json.dumps(schools_data, indent=2)}")
    
    context = {
        'schools_data': schools_data  # Pass Python list directly, not JSON string
    }
    
    
    return render(request, 'monitoring/map.html', context)
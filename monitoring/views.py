from django.shortcuts import render
from monitoring.models import School

# Create your views here.
def map_view(request):
    """
    Display interactive map with schools and pollution data - US-2
    
    Shows all schools as markers with latest pollution readings
    """
    schools = School.objects.all()
    
    # Prepare school data with latest pollution readings
    school_data = []
    for school in schools:
        school_data.append({
            'name': school.name,
            'location': school.location,
            'latitude': school.latitude,
            'longitude': school.longitude,
            'pm25': school.get_latest_reading('PM2.5'),
            'no2': school.get_latest_reading('NO2'),
        })
    
    context = {
        'schools': school_data,
        'schools_count': schools.count(),
    }
    
    return render(request, 'monitoring/map.html', context)



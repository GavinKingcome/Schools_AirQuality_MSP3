from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import School, AirQualityReading
from .forms import SchoolForm
from datetime import timedelta
from django.utils import timezone
import json


def map_view(request):
    """Display interactive map with schools and pollution data - US-READ"""
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


def school_list(request):
    """List all schools with edit/delete options - US-READ"""
    schools = School.objects.all().order_by('name')
    
    context = {
        'schools': schools,
    }
    return render(request, 'monitoring/school_list.html', context)


@login_required
def add_school(request):
    """Add a new school - US-CREATE"""
    if request.method == 'POST':
        form = SchoolForm(request.POST)
        if form.is_valid():
            school = form.save()
            messages.success(request, f'✓ {school.name} has been added successfully!')
            return redirect('map_view')  # Redirect to map
    else:
        form = SchoolForm()
    
    context = {
        'form': form,
        'action': 'Add',
    }
    return render(request, 'monitoring/school_form.html', context)


@login_required
def edit_school(request, school_id):
    """Edit existing school details - US-UPDATE"""
    school = get_object_or_404(School, id=school_id)
    
    if request.method == 'POST':
        form = SchoolForm(request.POST, instance=school)
        if form.is_valid():
            form.save()
            messages.success(request, f'✓ {school.name} has been updated successfully!')
            return redirect('school_list')
    else:
        form = SchoolForm(instance=school)
    
    context = {
        'form': form,
        'school': school,
        'action': 'Edit',
    }
    return render(request, 'monitoring/school_form.html', context)


@login_required
def delete_school(request, school_id):
    """Delete a school - US-DELETE"""
    school = get_object_or_404(School, id=school_id)
    
    if request.method == 'POST':
        school_name = school.name
        school.delete()
        messages.success(request, f'✓ {school_name} has been deleted.')
        return redirect('school_list')
    
    context = {
        'school': school,
    }
    return render(request, 'monitoring/school_confirm_delete.html', context)
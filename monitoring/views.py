from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from .models import School, AirQualityReading
from .forms import SchoolForm


def map_view(request):
    """Display interactive map with schools and pollution data - US-READ"""
    schools = School.objects.all()
    
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
        
        schools_data.append(school_dict)
    
    context = {
        'schools_data': schools_data  # Pass Python list directly, not JSON string
    }
    
    return render(request, 'map.html', context)  # ✅ FIXED


def school_list(request):
    """List all schools with edit/delete options - US-READ"""
    schools = School.objects.all().order_by('name')
    
    context = {
        'schools': schools,
    }
    return render(request, 'school_list.html', context)  # ✅ FIXED


def custom_logout(request):
    """Custom logout view that handles both GET and POST"""
    logout(request)
    messages.success(request, "You have been successfully logged out.")
    return redirect('map_view')

def signup_view(request):
    """User signup view"""
    if request.user.is_authenticated:
        return redirect('map_view')
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Welcome, {user.username}! Your account has been created successfully.')
            return redirect('map_view')
    else:
        form = UserCreationForm()
    
    return render(request, 'registration/signup.html', {'form': form})


@login_required
def add_school(request):
    """Add a new school - US-CREATE"""
    if request.method == 'POST':
        form = SchoolForm(request.POST)
        if form.is_valid():
            school = form.save(commit=False)
            school.created_by = request.user
            school.save()
            messages.success(request, f'✓ {school.name} has been added successfully!')
            return redirect('map_view')  # Redirect to map
    else:
        form = SchoolForm()
    
    context = {
        'form': form,
        'action': 'Add',
    }
    return render(request, 'add_school.html', context)  # ✅ FIXED


@login_required
def edit_school(request, school_id):
    """Edit existing school details - US-UPDATE"""
    school = get_object_or_404(School, id=school_id)
    
    if school.created_by != request.user:
       messages.error(request, "You can only edit schools that you added.")
       return redirect('school_list')
    
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
    return render(request, 'edit_school.html', context)  # ✅ FIXED


@login_required
def delete_school(request, school_id):
    """Delete a school - US-DELETE"""
    school = get_object_or_404(School, id=school_id)
    
    if school.created_by != request.user:
       messages.error(request, "You can only delete schools that you added.")
       return redirect('school_list')
    
    if request.method == 'POST':
        school_name = school.name
        school.delete()
        messages.success(request, f'✓ {school_name} has been deleted.')
        return redirect('school_list')
    
    context = {
        'school': school,
    }
    return render(request, 'school_confirm_delete.html', context)  # ✅ FIXED
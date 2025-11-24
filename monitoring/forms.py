from django import forms
from .models import School


class SchoolForm(forms.ModelForm):
    """Form for adding/editing schools - US-CREATE, US-UPDATE"""
    
    class Meta:
        model = School
        fields = ['name', 'location', 'latitude', 'longitude']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. Lyndhurst Primary School'
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. Lyndhurst Way, London SE15 5FA'
            }),
            'latitude': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. 51.4743',
                'step': '0.0001'
            }),
            'longitude': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. -0.0689',
                'step': '0.0001'
            }),
        }
        labels = {
            'name': 'School Name',
            'location': 'Full Address',
            'latitude': 'Latitude',
            'longitude': 'Longitude'
        }
        help_texts = {
            'latitude': 'Find coordinates on Google Maps',
            'longitude': 'Right-click location → "What\'s here?"'
        }
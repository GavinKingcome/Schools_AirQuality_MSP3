from django.test import TestCase
from monitoring.models import School

# Create your tests here.
class SchoolModelTest(TestCase):
    """Test the School model"""
    
    def test_create_school_with_name(self):
        """Test that we can create a school with a name"""
        # Create a school
        school = School.objects.create(name="Lyndhurst Primary School")
        
        # Check that the school was created with the correct name
        self.assertEqual(school.name, "Lyndhurst Primary School")
                                       
                                       

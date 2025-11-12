from django.test import TestCase
from monitoring.models import School, AirQualityReading
from datetime import datetime

class SchoolModelTest(TestCase):
    """Test the School model - US-1"""
    
    def test_create_school_with_name(self):
        """Test that we can create a school with a name"""
        school = School.objects.create(
            name="Lyndhurst Primary School",
            location="London, UK",
            latitude=51.4744,
            longitude=-0.0876
        )
        self.assertEqual(school.name, "Lyndhurst Primary School")
    
    def test_create_school_with_location(self):
        """Test that we can create a school with a location - US-1"""
        school = School.objects.create(
            name="Lyndhurst Primary School",
            location="80 Grove Lane, London SE5 8SN, UK",
            latitude=51.4744,
            longitude=-0.0876
        )
        self.assertEqual(school.location, "80 Grove Lane, London SE5 8SN, UK")
    
    def test_school_has_latitude(self):
        """Test that school stores latitude coordinate"""
        school = School.objects.create(
            name="Test School",
            location="Test Location",
            latitude=51.5074,
            longitude=-0.1278
        )
        self.assertEqual(school.latitude, 51.5074)
    
    def test_school_has_longitude(self):
        """Test that school stores longitude coordinate"""
        school = School.objects.create(
            name="Test School",
            location="Test Location",
            latitude=51.5074,
            longitude=-0.1278
        )
        self.assertEqual(school.longitude, -0.1278)
    
    def test_school_string_representation(self):
        """Test the string representation of a school"""
        school = School.objects.create(
            name="Lyndhurst Primary School",
            location="London, UK",
            latitude=51.4744,
            longitude=-0.0876
        )
        expected = "Lyndhurst Primary School (London, UK)"
        self.assertEqual(str(school), expected)


class AirQualityReadingModelTest(TestCase):
    """Test the AirQualityReading model - US-4"""
    
    def setUp(self):
        """Create a test school for all reading tests"""
        self.school = School.objects.create(
            name="Test School",
            location="Test Location",
            latitude=51.5,
            longitude=-0.1
        )
    
    def test_create_pm25_reading(self):
        """Test creating a PM2.5 pollution reading"""
        reading = AirQualityReading.objects.create(
            school=self.school,
            pollutant="PM2.5",
            value=35.2,
            measured_at=datetime(2025, 11, 12, 9, 0)
        )
        self.assertEqual(reading.pollutant, "PM2.5")
        self.assertEqual(reading.value, 35.2)
    
    def test_create_no2_reading(self):
        """Test creating a NO2 pollution reading"""
        reading = AirQualityReading.objects.create(
            school=self.school,
            pollutant="NO2",
            value=42.5,
            measured_at=datetime(2025, 11, 12, 9, 0)
        )
        self.assertEqual(reading.pollutant, "NO2")
        self.assertEqual(reading.value, 42.5)
    
    def test_reading_linked_to_school(self):
        """Test that reading is correctly linked to a school"""
        reading = AirQualityReading.objects.create(
            school=self.school,
            pollutant="PM2.5",
            value=35.2,
            measured_at=datetime(2025, 11, 12, 9, 0)
        )
        self.assertEqual(reading.school, self.school)
        self.assertEqual(reading.school.name, "Test School")
    
    def test_reading_has_timestamp(self):
        """Test that reading stores when it was measured"""
        measured_time = datetime(2025, 11, 12, 9, 30)
        reading = AirQualityReading.objects.create(
            school=self.school,
            pollutant="PM2.5",
            value=35.2,
            measured_at=measured_time
        )
        self.assertEqual(reading.measured_at, measured_time)
    
    def test_reading_string_representation(self):
        """Test the string representation of a reading"""
        reading = AirQualityReading.objects.create(
            school=self.school,
            pollutant="PM2.5",
            value=35.2,
            measured_at=datetime(2025, 11, 12, 9, 0)
        )
        expected = "Test School - PM2.5: 35.2 on 2025-11-12"
        self.assertEqual(str(reading), expected)


class SchoolAirQualityMethodsTest(TestCase):
    """Test School model methods for querying air quality data - US-7"""
    
    def setUp(self):
        """Create test school and sample readings"""
        self.school = School.objects.create(
            name="Test School",
            location="Test Location",
            latitude=51.5,
            longitude=-0.1
        )
    
    def test_get_latest_pm25_reading(self):
        """Test getting the most recent PM2.5 reading - US-7"""
        # Create older reading
        AirQualityReading.objects.create(
            school=self.school,
            pollutant="PM2.5",
            value=30.0,
            measured_at=datetime(2025, 11, 10, 9, 0)
        )
        # Create newer reading
        AirQualityReading.objects.create(
            school=self.school,
            pollutant="PM2.5",
            value=35.2,
            measured_at=datetime(2025, 11, 12, 9, 0)
        )
        
        latest = self.school.get_latest_reading("PM2.5")
        self.assertEqual(latest, 35.2)
    
    def test_get_latest_no2_reading(self):
        """Test getting the most recent NO2 reading - US-7"""
        AirQualityReading.objects.create(
            school=self.school,
            pollutant="NO2",
            value=42.5,
            measured_at=datetime(2025, 11, 12, 9, 0)
        )
        
        latest = self.school.get_latest_reading("NO2")
        self.assertEqual(latest, 42.5)
    
    def test_get_latest_reading_with_no_data(self):
        """Test getting latest reading when no data exists"""
        latest = self.school.get_latest_reading("PM2.5")
        self.assertIsNone(latest)
    
    def test_get_average_pm25_reading(self):
        """Test calculating average PM2.5 pollution - US-7"""
        AirQualityReading.objects.create(
            school=self.school,
            pollutant="PM2.5",
            value=30.0,
            measured_at=datetime(2025, 11, 10, 9, 0)
        )
        AirQualityReading.objects.create(
            school=self.school,
            pollutant="PM2.5",
            value=40.0,
            measured_at=datetime(2025, 11, 11, 9, 0)
        )
        
        average = self.school.get_average_reading("PM2.5")
        self.assertEqual(average, 35.0)  # (30 + 40) / 2
    
    def test_get_average_with_multiple_readings(self):
        """Test average calculation with multiple readings"""
        values = [30.0, 35.0, 40.0, 45.0]
        for i, value in enumerate(values):
            AirQualityReading.objects.create(
                school=self.school,
                pollutant="PM2.5",
                value=value,
                measured_at=datetime(2025, 11, 10 + i, 9, 0)
            )
        
        average = self.school.get_average_reading("PM2.5")
        expected = sum(values) / len(values)
        self.assertEqual(average, expected)
    
    def test_get_peak_pm25_reading(self):
        """Test getting the highest PM2.5 reading - US-7"""
        AirQualityReading.objects.create(
            school=self.school,
            pollutant="PM2.5",
            value=30.0,
            measured_at=datetime(2025, 11, 10, 9, 0)
        )
        AirQualityReading.objects.create(
            school=self.school,
            pollutant="PM2.5",
            value=52.7,  # Peak!
            measured_at=datetime(2025, 11, 11, 9, 0)
        )
        AirQualityReading.objects.create(
            school=self.school,
            pollutant="PM2.5",
            value=35.2,
            measured_at=datetime(2025, 11, 12, 9, 0)
        )
        
        peak = self.school.get_peak_reading("PM2.5")
        self.assertEqual(peak, 52.7)
    
    def test_get_peak_reading_detail(self):
        """Test getting full details of peak reading including date - US-7"""
        AirQualityReading.objects.create(
            school=self.school,
            pollutant="PM2.5",
            value=30.0,
            measured_at=datetime(2025, 11, 10, 9, 0)
        )
        peak_reading = AirQualityReading.objects.create(
            school=self.school,
            pollutant="PM2.5",
            value=52.7,
            measured_at=datetime(2025, 11, 11, 9, 0)
        )
        
        peak_detail = self.school.get_peak_reading_detail("PM2.5")
        self.assertEqual(peak_detail.value, 52.7)
        self.assertEqual(peak_detail.measured_at.date(), datetime(2025, 11, 11,).date())
    
    def test_multiple_pollutants_independent(self):
        """Test that different pollutants are tracked independently"""
        # Add PM2.5 readings
        AirQualityReading.objects.create(
            school=self.school,
            pollutant="PM2.5",
            value=35.2,
            measured_at=datetime(2025, 11, 12, 9, 0)
        )
        # Add NO2 readings
        AirQualityReading.objects.create(
            school=self.school,
            pollutant="NO2",
            value=42.5,
            measured_at=datetime(2025, 11, 12, 9, 0)
        )
        
        pm25_latest = self.school.get_latest_reading("PM2.5")
        no2_latest = self.school.get_latest_reading("NO2")
        
        self.assertEqual(pm25_latest, 35.2)
        self.assertEqual(no2_latest, 42.5)
        # Verify they're different
        self.assertNotEqual(pm25_latest, no2_latest)
    
    def test_get_top_readings(self):
        """Test getting top N highest readings - US-7"""
        values = [30.0, 35.0, 40.0, 45.0, 50.0]
        for i, value in enumerate(values):
            AirQualityReading.objects.create(
                school=self.school,
                pollutant="PM2.5",
                value=value,
                measured_at=datetime(2025, 11, 10 + i, 9, 0)
            )
        
        top_3 = self.school.get_top_readings("PM2.5", limit=3)
        top_values = [reading.value for reading in top_3]
        
        self.assertEqual(len(top_values), 3)
        self.assertEqual(top_values, [50.0, 45.0, 40.0])  # Descending order


class MultipleSchoolsTest(TestCase):
    """Test that multiple schools can have independent air quality data"""
    
    def test_readings_belong_to_correct_school(self):
        """Test that readings are correctly associated with their school"""
        school1 = School.objects.create(
            name="School 1",
            location="Location 1",
            latitude=51.5,
            longitude=-0.1
        )
        school2 = School.objects.create(
            name="School 2",
            location="Location 2",
            latitude=51.6,
            longitude=-0.2
        )
        
        # Add readings to school 1
        AirQualityReading.objects.create(
            school=school1,
            pollutant="PM2.5",
            value=35.2,
            measured_at=datetime(2025, 11, 12, 9, 0)
        )
        
        # Add readings to school 2
        AirQualityReading.objects.create(
            school=school2,
            pollutant="PM2.5",
            value=28.3,
            measured_at=datetime(2025, 11, 12, 9, 0)
        )
        
        # Verify each school has correct data
        self.assertEqual(school1.get_latest_reading("PM2.5"), 35.2)
        self.assertEqual(school2.get_latest_reading("PM2.5"), 28.3)
        
        # Verify readings don't mix
        self.assertNotEqual(
            school1.get_latest_reading("PM2.5"),
            school2.get_latest_reading("PM2.5")
        )
from django.test import TestCase
from unittest.mock import patch, Mock
from monitoring.models import School, AirQualityReading
from datetime import datetime
from django.utils import timezone


class AirQualityAPITest(TestCase):
    """Test fetching air quality data from OpenAQ API - US-5"""
    
    def setUp(self):
        """Create a test school before each test"""
        self.school = School.objects.create(
            name="Test School",
            location="London, UK",
            latitude=51.5074,
            longitude=-0.1278
        )
    
    @patch('requests.get')
    def test_fetch_pm25_data_success(self, mock_get):
        """Test successfully fetching PM2.5 data from API - US-5"""
        # Simulate successful API response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'results': [
                {
                    'parameter': 'pm25',
                    'value': 35.2,
                    'date': {'utc': '2025-11-12T09:00:00Z'}
                }
            ]
        }
        mock_get.return_value = mock_response
        
        # Import function we'll create (will fail - that's TDD!)
        from monitoring.management.commands.fetch_air_quality import fetch_data_for_school
        
        result = fetch_data_for_school(self.school)
        self.assertTrue(result)
    
    @patch('requests.get')
    def test_store_pm25_reading_in_database(self, mock_get):
        """Test that PM2.5 data is saved to database - US-5"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'results': [
                {
                    'parameter': 'pm25',
                    'value': 35.2,
                    'date': {'utc': '2025-11-12T09:00:00Z'}
                }
            ]
        }
        mock_get.return_value = mock_response
        
        from monitoring.management.commands.fetch_air_quality import fetch_data_for_school
        
        fetch_data_for_school(self.school)
        
        # Check database
        reading = AirQualityReading.objects.filter(
            school=self.school,
            pollutant='PM2.5'
        ).first()
        
        self.assertIsNotNone(reading)
        self.assertEqual(reading.value, 35.2)
    
    @patch('requests.get')
    def test_fetch_no2_data(self, mock_get):
        """Test fetching NO2 data - US-5"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'results': [
                {
                    'parameter': 'no2',
                    'value': 42.5,
                    'date': {'utc': '2025-11-12T09:00:00Z'}
                }
            ]
        }
        mock_get.return_value = mock_response
        
        from monitoring.management.commands.fetch_air_quality import fetch_data_for_school
        
        fetch_data_for_school(self.school)
        
        reading = AirQualityReading.objects.filter(
            school=self.school,
            pollutant='NO2'
        ).first()
        
        self.assertIsNotNone(reading)
        self.assertEqual(reading.value, 42.5)
    
    @patch('requests.get')
    def test_api_connection_failure(self, mock_get):
        """Test handling of API errors - US-5"""
        # Simulate connection error
        mock_get.side_effect = Exception("Connection timeout")
        
        from monitoring.management.commands.fetch_air_quality import fetch_data_for_school
        
        result = fetch_data_for_school(self.school)
        self.assertFalse(result)
    
    @patch('requests.get')
    def test_no_duplicate_readings(self, mock_get):
        """Test that same reading isn't stored twice - US-5"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'results': [
                {
                    'parameter': 'pm25',
                    'value': 35.2,
                    'date': {'utc': '2025-11-12T09:00:00Z'}
                }
            ]
        }
        mock_get.return_value = mock_response
        
        from monitoring.management.commands.fetch_air_quality import fetch_data_for_school
        
        # Fetch twice
        fetch_data_for_school(self.school)
        fetch_data_for_school(self.school)
        
        # Should only have 1 reading
        count = AirQualityReading.objects.filter(
            school=self.school,
            pollutant='PM2.5'
        ).count()
        
        self.assertEqual(count, 1)
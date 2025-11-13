from django.test import TestCase
from django.urls import reverse
from monitoring.models import School

class MapViewTest(TestCase):
    def test_map_view_with_no_schools(self):
        response = self.client.get(reverse('map_view'))
        self.assertContains(response, 'No Schools Found')
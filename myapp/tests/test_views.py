from django.test import TestCase, Client
from django.urls import reverse
from myapp.views import index
from myapp.models import Holidays
import json
import requests


class TestViews(TestCase):
    
    def test_holiday_list(self):
        client = Client()
        response = client.get(reverse('holiday_list'))
        
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'myapp/holidays.html')
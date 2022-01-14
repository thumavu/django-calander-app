from django.test import SimpleTestCase
from django.urls import reverse, resolve
from myapp.views import index

class TestUrls(SimpleTestCase):
    
    def test_index_url_resolves(self):
        url = reverse('holiday_list')
        print(resolve(url))
        self.assertEquals(resolve(url).func, index )
        
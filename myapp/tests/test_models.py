from myapp.models import Holidays
from django.test import TestCase

class TestModel(TestCase):
    
    def test_holiday(self):
        holiday_instance = Holidays(uuid='19930415', name='Thulasizwe birthday holiday', date='1993-04-15', observed='1993-04-15', public='true',
                            country='ZA', date_name='Friday', date_observed='Friday')
        holiday_instance.save()
        self.assertEquals(str(holiday_instance), 'Thulasizwe birthday holiday')
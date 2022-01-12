from django.shortcuts import render
from .models import Holidays
import requests
import pprintpp

def index(request):
    url = "https://holidayapi.com/v1/holidays?pretty&country=ZA&year=2021&key=7fab0a99-13f4-4f91-afc3-00fd1f5bf66d"
    response = requests.get(url).json()
    holidays = response['holidays']
    
    holiday_list = []
    
    for holiday in holidays:
        # Create a holidays dict to be displayed
        holiday_disctionary = {
            'name' : holiday['name'],
            'date' : holiday['date'],
            'observed' : holiday['observed'],
            'public' : holiday['public'],
            'country' : holiday['country'],
            'uuid' : holiday['uuid'],
            'date_name' : holiday['weekday']['date']['name'],
            'date_observed' : holiday['weekday']['observed']['name']
        }
        holiday_list.append(holiday_disctionary)
        
        # Save data on the database table created by the models
        instance = Holidays(name=holiday['name'], date=holiday['date'], observed=holiday['observed'], public=holiday['public'],
                            country=holiday['country'], uuid=holiday['uuid'], date_name=holiday['weekday']['date']['name'], date_observed=holiday['weekday']['observed']['name'])
        instance.save()
        
        pprintpp.pprint(holiday_disctionary)
        
    context = {'holiday_list' : holiday_list}
    return render(request, 'myapp/holidays.html', context)

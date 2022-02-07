from django.shortcuts import render
from django.http import HttpResponse
from .models import Holidays
from dotenv import load_dotenv
import os
import requests
import logging

logger = logging.getLogger(__name__)
load_dotenv()

def index(request):
    
    if request.method == 'POST':
        country_code = request.POST["country_code"]
        
        api_key = os.getenv("API_KEY")
        url = f"https://holidayapi.com/v1/holidays?pretty&country={country_code}&year=2021&key={api_key}"
        response = requests.get(url).json()
        status = response['status']
            
        if status is not 200:
            error = response['error']
            logger.error(f'{status} : {error} ')
            return render(request, 'myapp/error.html', {'error' : error})

        holidays = response['holidays']
        holiday_list = []

        for holiday in holidays:
            # Create a holidays dict to be displayed
            name = holiday['name']
            date = holiday['date']
            observed = holiday['observed']
            uuid = holiday['uuid']
            country = holiday['country']
            date_name = holiday['weekday']['date']['name']
            date_observed = holiday['weekday']['observed']['name']
            
            if holiday['public'] == True:
                public = "Observed as a public holiday"
            else: 
                public = "Not observed as a public holiday"
                
            holiday_disctionary = {
                'name' : name,
                'date' : date,
                'observed' : observed,
                'public' : public,
                'uuid' : uuid,
                'country' : country,
                'date_name' : date_name,
                'date_observed' : date_observed
            }
            holiday_list.append(holiday_disctionary)
            
            # Save data on the database table created by the models
            holiday_instance = Holidays(uuid=uuid, name=name, date=date, observed=observed, public=public,
                                country=country, date_name=date_name, date_observed=date_observed)
            holiday_instance.save()
            
        #logger.debug(holiday_disctionary)
        context = {'holiday_list' : holiday_list}
    else:
        context = {'holiday_list' : ""}
    return render(request, 'myapp/holidays.html', context)

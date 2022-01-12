#import requests
#import json
#import pprintpp

# ----- Learning curve, this is where I started with the project.
# ----- The concept of python indent sensitive was a has frustration for me, while working on this project I realized that the Django framework is a semester on it's own -----

#https://holidayapi.com/v1/holidays?pretty&country=ZA&year=2021&key=7fab0a99-13f4-4f91-afc3-00fd1f5bf66d
#class CalanderHolidays:
#    def __init__(self, name, date, observed, public, country, uuid, weekday):
#        self.name = name
#        self.date = date
#        self.observed = observed
#        self.public = public
#        self.country = country
#        self.uuid = uuid
#        self.date_name = weekday['date']['name']
#        self.date_observed = weekday['observed']['name']
    

#    @classmethod
#    def holidays(cls):
#        URL = "https://holidayapi.com/v1/holidays?pretty&country=ZA&year=2021&key=7fab0a99-13f4-4f91-afc3-00fd1f5bf66d"
#        response = requests.get(URL).json()
#        holidays = response['holidays']
#        response_status = response['status']
#        response_warning = response['warning']
#        holiday_list = []
        
#        for holiday in holidays:
#            holiday_list.append(cls(**holiday))
#        return holiday_list
    
#    def __repr__(self):
#        return f'<Holiday: { self.name }>'

#pprintpp.pprint(str(CalanderHolidays.holidays()))
#print(CalanderHolidays.holidays()[0])
#print(len(CalanderHolidays.holidays()))
#print(type(CalanderHolidays.holidays()))
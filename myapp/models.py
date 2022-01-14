from django.db import models

class Holidays(models.Model):
    uuid = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=100)
    date = models.DateField()
    observed = models.DateField()
    public = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    date_name = models.CharField(max_length=100)
    date_observed = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
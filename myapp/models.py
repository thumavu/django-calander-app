from django.db import models

class Holidays(models.Model):
    name = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    observed = models.CharField(max_length=100)
    public = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    uuid = models.CharField(max_length=100)
    date_name = models.CharField(max_length=100)
    date_observed = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
 #   class Meta:
 #       verbose_name_plural = 'holidays'
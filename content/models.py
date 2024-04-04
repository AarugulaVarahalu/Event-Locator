from django.db import models

# Create your models here.



class Event(models.Model):

    event_name = models.CharField(max_length=200, blank=False)
    city_name = models.TextField(blank=False)
    date = models.DateField(blank=False)
    time = models.TimeField(blank=False)
    latitude = models.TextField()
    longitude = models.TextField()
    
    class meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'



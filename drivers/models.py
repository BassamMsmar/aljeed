from django.db import models
from django.shortcuts import reverse

# Create your models here.

class Driver(models.Model):

    driver_name = models.CharField(max_length=50)
    driver_images = models.ImageField(upload_to = 'drivers/', null=True)
    resident_number = models.CharField(max_length=50)
    phone_number = models.PositiveIntegerField()
    plate_number =  models.CharField(max_length=50)
    track_type = models.CharField(max_length=50)

    

    def __str__(self):
        return self.driver_name




from django.db import models
from django.shortcuts import reverse

# Create your models here.

class Driver(models.Model):

    driver_name = models.models.CharField(max_length=50)
    resident_number = models.CharField(max_length=50)
    phone_number = models.PhoneNumberField()
    plate_number =  models.CharField(max_length=50)
    track_type = models.CharField(max_length=50)

    

    class Meta:
        verbose_name = _("Driver")
        verbose_name_plural = _("Drivers")

    def __str__(self):
        return self.driver_name

    def get_absolute_url(self):
        return reverse("Driver_detail", kwargs={"pk": self.pk})

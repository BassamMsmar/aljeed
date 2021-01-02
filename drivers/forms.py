from django import forms
from .models import Driver

class AddDriverForm(forms.ModelForm):


    class Meta:
        model =  Driver
        fields = (
            'driver_name',
            'driver_images',
            'resident_number',
            'phone_number',
            'plate_number',
            'driver_name'
        )

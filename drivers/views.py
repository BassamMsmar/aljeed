from django.contrib.admin import decorators
from django.contrib.admin.options import FORMFIELD_FOR_DBFIELD_DEFAULTS
from drivers.models import Driver
from django.http import request
from django.shortcuts import get_object_or_404, render

from .models import Driver
from .forms import AddDriverForm

# Create your views here.
def drivers_list(request):
    drivers = Driver.objects.all()
    return render(request, 'drivers/drivers-list.html', {"drivers": drivers})

def driver_details(request, pk):
    driver = get_object_or_404(Driver, pk=pk)
    return render(request, 'drivers/driver-details.html', {"driver": driver})


def add_driver(request):
    if request.method == 'POST':
        form = AddDriverForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return render(request, 'drivers/driver-crud-successful.html', {'form': form})

    form = AddDriverForm
    return render(request, 'drivers/driver-add.html', {'form': form})







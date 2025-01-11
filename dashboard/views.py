from django.shortcuts import render
from .models import *

# Create your views here.
def dashboard_view(request):
    vehicles=ElectricVichele.objects.all()
    chart_labels= [vehicle.make for vehicle in vehicles]
    chart_data = [vehicle.electric_range for vehicle in vehicles]

    context={
        'vehicles':vehicles,
        'chart_labels':chart_labels,
        'chart_data': chart_data,
    }

    return render(request , 'index.html', context)

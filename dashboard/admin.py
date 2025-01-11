from django.contrib import admin
from .models import *

class ElectricVehicleAdmin(admin.ModelAdmin):
    list_display=('make','model','year','electric_range','vichele_type')
admin.site.register(ElectricVichele,ElectricVehicleAdmin)

# Register your models here.

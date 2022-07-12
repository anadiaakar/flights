from django.contrib import admin

# Register your models here.
from .models import FlightDetails , City

admin.site.register(FlightDetails)
admin.site.register(City)
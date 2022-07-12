from django.urls import path
from . import views

urlpatterns = [
    path('create-flight' , views.Flights.as_view()),
    path('update-flight/<int:id>' , views.Update.as_view()),
    path('flight-plan' , views.FlightPlan.as_view()),
    path('flight-find' , views.FindPlan.as_view()),
    
     
]
from django.db import models

# Create your models here.


class City(models.Model):
	name = models.CharField(max_length=100)
	def __str__(self):
		return self.name

class FlightDetails(models.Model):
	number = models.CharField(max_length=100)
	departure_city = models.ForeignKey(City, related_name='dep', on_delete=models.CASCADE)
	departure_time = models.DateTimeField()
	arrival_city = models.ForeignKey(City, related_name='arr', on_delete=models.CASCADE)
	arrival_time = models.DateTimeField()
 
	def __str__(self):
		return self.number


class Passenger(models.Model):
	Passenger_name = models.CharField(max_length=100)
	passenger_passport_id = models.CharField(max_length=10,unique=True)
	passenger_gender = models.CharField(max_length=2)
	passenger_contact = models.CharField(max_length=100)
 
class BookingDetails(models.Model):
	number = models.CharField(max_length=100)
	passenger = models.ForeignKey(Passenger, related_name='pas', on_delete=models.CASCADE)
	booking_confirmation_time = models.DateTimeField()
	booking_status = models.Boolean()
	flight = models.ForeignKey(FlightDetails, related_name='arr', on_delete=models.CASCADE)
 
	def __str__(self):
		return self.number


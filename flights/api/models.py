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



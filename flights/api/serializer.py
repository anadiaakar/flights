from rest_framework import serializers
from .models import FlightDetails , City

class FlightDetailsSerializer(serializers.ModelSerializer):
    number = serializers.CharField(max_length=100, required=True, allow_blank=False, allow_null=False)
    arrival_city = serializers.CharField(max_length=100, required=True, allow_blank=False, allow_null=False)
    departure_city = serializers.CharField(max_length=100, required=True, allow_blank=False, allow_null=False,)
    departure_time = serializers.DateTimeField()
    arrival_time = serializers.DateTimeField()
    
    def to_representation(self, instance):
        rep = super(FlightDetailsSerializer, self).to_representation(instance)
        rep['arrival_city'] = instance.arrival_city.name
        rep['departure_city'] = instance.departure_city.name
        return rep
    
    def create(self, validated_data):
        departure_city = City.objects.get_or_create(name=validated_data.pop("departure_city"))
        arrival_city = City.objects.get_or_create(name=validated_data.pop("arrival_city"))
        details_instance = FlightDetails.objects.create(**validated_data, departure_city= departure_city ,arrival_city = arrival_city)
        return details_instance
    
    def update(self, validated_data):
        details_instance = FlightDetails.objects.get(id= validated_data.pop("id"))
        details_instance.departure_city = City.objects.get_or_create(name=validated_data.pop("departure_city"))
        details_instance.arrival_city = City.objects.get_or_create(name=validated_data.pop("arrival_city"))
        details_instance.departure_time = validated_data.get('departure_time')
        details_instance.arrival_time = validated_data.get("arrival_time")
        return details_instance
    
    def validate(self, data):
        
        #Check that depart is before arrival.
        
        if data['arrival_time'] > data['departure_time']:
            raise serializers.ValidationError("depart must be before arrival.")
        
        #Check that depart City is not arrival City.
        
        if data['departure_city'] == data['arrival_city']:
            raise serializers.ValidationError("depart city and arrival city must be different.")
        
        return data
    
    class Meta:
        model = FlightDetails
        fields = '__all__'
    
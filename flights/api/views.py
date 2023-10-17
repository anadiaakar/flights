from django.http import JsonResponse
from django.core import serializers
from rest_framework.views import APIView
from .serializer import FlightDetailsSerializer
from .models import FlightDetails , City , Passenger
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

# Create your views here.

class Flights(APIView):
    def post(self,request):
        
        serializer = FlightDetailsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.create()
            return JsonResponse(serializer.validated_data)
        
class Update(APIView):
    def put(self,request):
        print(request.data)
        serializer = FlightDetailsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.update()
            return JsonResponse(serializer.validated_data)

class FlightPlan(APIView):
    renderer_classes = [TemplateHTMLRenderer]

	def get(self,request):        
        print(request.query_params)
        dep_city = request.query_params.get("departure")
        departure_time = request.query_params.get("departure_t")
        arrival_city =  request.query_params.get("destination")
        print(dep_city)
        dep_c_ins = City.objects.get_or_create(name=dep_city)
        arr_c_ins = City.objects.get_or_create(name=arrival_city)
        print(dep_c_ins)        
        print(departure_time)
        result = []
        flight_option = FlightDetails.objects.filter(departure_city = dep_c_ins[0] , departure_time=departure_time , arrival_city=arr_c_ins[0]).first()
        if flight_option:
            serialized_obj = FlightDetailsSerializer(flight_option).data
            # option_serializer = FlightDetailsSerializer(option, many=True)
            print(serialized_obj)
            result.append(serialized_obj)
            # result.append(option_serializer[0])
            print({'Response':result})
            return Response({'Response':result}, template_name='view.html')
        options  = FlightDetails.objects.filter(departure_city = dep_c_ins[0] , departure_time=departure_time)
        
        print(options)
        if options:
            for option in options:
                fligt = FlightDetails.objects.filter(departure_city = option.arrival_city , arrival_city=arr_c_ins[0]).order_by('arrival_time')
                if not fligt:
                    pass
                else:
                    fligt_serializer = FlightDetailsSerializer(fligt.first())
                    option_serializer = FlightDetailsSerializer(option)
                    result.append(fligt_serializer.data)
                    result.append(option_serializer.data)
        else:
            result = ["No flights Available"]
            print({'Response':result})
        return Response({'Response':result}, template_name='view.html')
class FindPlan(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'view.html'
    
    def get(self,request):
        return Response({})

def AddPassenger(APIView):
    def post(self,request):
        passenger_name = request.data.get("passenger_name")
        passenger_passport_id = request.data.get("passenger_passport_id")
        passneger_gender = request.data.ger("passenger_gender")
        passenger_contanct = request.data.ger("passenger_conatact")
        try:
            passenger = Passenger.objects.get(passenger_passport_id=passenger_passport_id)
            serializer = PassengerSerializer(passenger)
            return JsonResponse(serializer.validated_data)
        except:
            serializer = PassengerSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.create()
                return JsonResponse(serializer.validated_data)
        

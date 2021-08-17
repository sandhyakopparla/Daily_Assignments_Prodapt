from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse
import json
from passengerapp.serializers import PassengerSerializer
from passengerapp.models import Passenger
from rest_framework.parsers import JSONParser 
from rest_framework import status
@csrf_exempt 
def passenger_details(request,fetchid):
    try:
        passengerapp=Passenger.objects.get(id=fetchid)
        if(request.method=="GET"):
            passenger_serializer=PassengerSerializer(passengerapp)
            return JsonResponse(passenger_serializer.data,safe=False,status=status.HTTP_200_OK)
        if (request.method=="DELETE"):
            passengerapp.delete()
            return HttpResponse("Deleted",status=status.HTTP_200_OK)
        if (request.method=="PUT"):
            mydict=JSONParser().parse(request)
            passenger_serializer=PassengerSerializer(passengerapp,data=mydict)
            if(passenger_serializer.is_valid()):
                passenger_serializer.save()
                return JsonResponse(passenger_serializer.data,status=status.HTTP_200_OK)
            else:
                return JsonResponse(passenger_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    except Passenger.DoesNotExist:
        return HttpResponse("invalid passenger Id",status=status.HTTP_404_NOT_FOUND) 
@csrf_exempt
def passenger_list(request):
    if(request.method=="GET"):
        passengerapp=Passenger.objects.all()
        passenger_serializer=PassengerSerializer(passengerapp,many=True)
        return JsonResponse(passenger_serializer.data,safe=False)
@csrf_exempt
def passengerPage(request):
    if(request.method=="POST"):
       mydict=JSONParser().parse(request)   
       passenger_serialize=PassengerSerializer(data=mydict)  
       if(passenger_serialize.is_valid()):
           passenger_serialize.save()
           return JsonResponse(passenger_serialize.data,status=status.HTTP_200_OK)
       else:
           return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return Httpresponse("No Get method allowed",status=status.HTTP_400_BAD-REQUEST) 

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse
import json
from driverapp.serializers import DriverSerializer
from driverapp.models import Driver
from rest_framework.parsers import JSONParser 
from rest_framework import status
@csrf_exempt
def driver_details(request,fetchid):
    try:
        driverapp=Driver.objects.get(id=fetchid)
        if(request.method=="GET"):
            driver_serializer=DriverSerializer(driverapp)
            return JsonResponse(driver_serializer.data,safe=False,status=status.HTTP_200_OK)
        if (request.method=="DELETE"):
            driverapp.delete()
            return HttpResponse("Deleted",status=status.HTTP_200_OK)
        if (request.method=="PUT"):
            mydict=JSONParser().parse(request)
            driver_serializer=DriverSerializer(driverapp,data=mydict)
            if(driver_serializer.is_valid()):
                driver_serializer.save()
                return JsonResponse(driver_serializer.data,status=status.HTTP_200_OK)
            else:
                return JsonResponse(driver_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    except Driver.DoesNotExist:
        return HttpResponse("invalid driver Id",status=status.HTTP_404_NOT_FOUND)
@csrf_exempt
def driver_list(request):
    if(request.method=="GET"):
        driverapp=Driver.objects.all()
        driver_serializer=DriverSerializer(driverapp,many=True)
        return JsonResponse(driver_serializer.data,safe=False)
@csrf_exempt
def driverPage(request):
    if(request.method=="POST"):
       mydict=JSONParser().parse(request)   
       driver_serialize=DriverSerializer(data=mydict)  
       if(driver_serialize.is_valid()):
           driver_serialize.save()
           return JsonResponse(driver_serialize.data,status=status.HTTP_200_OK)
       else:
           return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return Httpresponse("No Get method allowed",status=status.HTTP_400_BAD-REQUEST)
        



from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from doctors.serializers import DoctorSerializer
from doctors.models import Doctor
from rest_framework.parsers import JSONParser
from rest_framework import status
# Create your views here.
@csrf_exempt
def doctors_details(request,fetchid):
    try:
        doctors=Doctor.objects.get(id=fetchid)
    except Doctor.DoesNotExist:
        return HttpResponse("Invalid Doctor id",status=status.HTTP_404_NOT_FOUND)
    if(request.method=="GET"):
        doctors_serializer=DoctorSerializer(doctors)
        return JsonResponse(doctors_serializer.data,safe=False,status=status.HTTP_200_OK)
    if(request.method=="DELETE"):
        doctors.delete()
        return HttpResponse("deleted",status=status.HTTP_204_NO_CONTENT)
    if(request.method=="PUT"):
        mydict=JSONParser().parse(request)
        doctors_serialize=DoctorSerializer(doctors,data=mydict)
        if(doctors_serialize.is_valid()):
            doctors_serialize.save()
            return JsonResponse(doctors_serialize.data,status=status.HTTP_200_OK)

@csrf_exempt
def doctors_list(request):
    if(request.method=='GET'):
        doctors=Doctor.objects.all()
        doctors_serializer=DoctorSerializer(doctors,many=True)
        return JsonResponse(doctors_serializer.data,safe=False)


@csrf_exempt
def addDoctor(request):
    if(request.method=='POST'):
        mydict=JSONParser().parse(request)
        doctors_serialize=DoctorSerializer(data=mydict)
        if(doctors_serialize.is_valid()):
            doctors_serialize.save()
            return JsonResponse(doctors_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("error in serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("GET method",status=status.HTTP_404_NOT_FOUND)
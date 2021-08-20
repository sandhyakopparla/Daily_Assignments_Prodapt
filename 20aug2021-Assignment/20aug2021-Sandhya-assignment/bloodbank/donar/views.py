from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse
import json
from donar.serializers import donarSerializer
from donar.models import Donar
from rest_framework.parsers import JSONParser 
from rest_framework import status
def blood_view(request):
    return render(request,'register.html')
# Create your views here.
def search_view(request):
    return render(request,'search.html')
@csrf_exempt
def donarPage(request):
    if(request.method=="POST"):
       mydict=JSONParser().parse(request)   
       donar_serialize=donarSerializer(data=mydict)  
       if(donar_serialize.is_valid()):
           donar_serialize.save()
           return JsonResponse(donar_serialize.data,status=status.HTTP_200_OK)
       else:
           return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return Httpresponse("No Get method allowed",status=status.HTTP_400_BAD-REQUEST)
@csrf_exempt
def donar_list(request):
    if(request.method=="GET"):
        donar=Donar.objects.all()
        donar_serializer=donarSerializer(donar,many=True)
        return JsonResponse(donar_serializer.data,safe=False)
@csrf_exempt
def donar_details(request,fetchblood_group):
    try:
        donar=Donar.objects.get(blood_group=fetchblood_group)
        if(request.method=="GET"):
            donar_serializer=donarSerializer(donar)
            return JsonResponse(donar_serializer.data,safe=False,status=status.HTTP_200_OK)
        if (request.method=="DELETE"):
            donar.delete()
            return HttpResponse("Deleted",status=status.HTTP_200_OK)
        if (request.method=="PUT"):
            mydict=JSONParser().parse(request)
            donar_serializer=donarSerializer(donar,data=mydict)
            if(donar_serializer.is_valid()):
                donar_serializer.save()
                return JsonResponse(donar_serializer.data,status=status.HTTP_200_OK)
            else:
                return JsonResponse(donar_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    except Donar.DoesNotExist:
        return HttpResponse("invalid blood group",status=status.HTTP_404_NOT_FOUND)
# Create your views here.

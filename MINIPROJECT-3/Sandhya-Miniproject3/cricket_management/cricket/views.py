from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse
import json
from cricket.serializers import cricketSerializer
from cricket.models import Cricket
from rest_framework.parsers import JSONParser 
from rest_framework import status
import requests


@csrf_exempt
def cricketPage(request):
    if(request.method=="POST"):
        # mydict=JSONParser().parse(request)
        cricket_serialize=cricketSerializer(data=request.POST)
        if(cricket_serialize.is_valid()):
            cricket_serialize.save()
            return redirect(view_all)
        else:
            return HttpResponse("Error in Serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("No Get method Allowed",status=status.HTTP_404_PAGE_NOT_FOUND)
@csrf_exempt
def cricket_list(request):
    if(request.method=="GET"):
        cricket=Cricket.objects.all()
        cricket_serialize=cricketSerializer(cricket,many=True)
        return JsonResponse(cricket_serialize.data,safe=False)
@csrf_exempt
def cricket_details(request,fetchid):
    try:
        cricket=Cricket.objects.get(id=fetchid)
        if(request.method=="GET"):
            cricket_serializer=cricketSerializer(cricket)
            return JsonResponse(cricket_serializer.data,safe=False,status=status.HTTP_200_OK)
        if(request.method=="PUT"):
            mydict=JSONParser().parse(request)
            cricket_serializer=cricketSerializer(cricket,data=mydict)
            if(cricket_serializer.is_valid()):
                cricket_serializer.save()
                return JsonResponse(cricket_serializer.data,status=status.HTTP_200_OK)
            else:
                return JsonResponse(cricket_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        if(request.method=="DELETE"):
            cricket.delete()
            return HttpResponse("Deleted",status=status.HTTP_200_OK)
    except Cricket.DoesNotExist:
        return HttpResponse("invalid cricket id",status=status.HTTP_404_NOT_FOUND)
def register_view(request):
    return render(request,'register.html')
def view_all(request):
    fetchdata=requests.get("http://127.0.0.1:8000/cricket/viewall/").json()
    return render(request,'viewall.html',{"data":fetchdata})
def update_all(request):
    return render(request,'update.html')
def delete_all(request):
    return render(request,'delete.html')


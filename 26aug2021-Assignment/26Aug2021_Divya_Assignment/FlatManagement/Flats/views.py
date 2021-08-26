from re import T
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from Flats.serializer import FlatSerializer
from Flats.models import Flatsmanage
from rest_framework.parsers import JSONParser
from rest_framework import status
import json
import requests
# Create your views here.
def home(request):
    return render(request,'Home.html')
def add(request):
    return render(request,'add.html')
def show(request):
    fetchdata = requests.get("http://127.0.0.1:8000/flat/viewall/").json()
    return render(request,'show_details.html',{"data":fetchdata})
def searchone(request):
    return render(request,'search_detail.html')
def updateone(request):
    return render(request,'update_detail.html')
def deleteone(request):
    return render(request,'delete_detail.html')

@csrf_exempt
def add_details(request):
    if(request.method == "POST"):
        #mydata = JSONParser().parse(request)
        #flat_serializer = FlatSerializer(data=mydata)
        flat_serializer = FlatSerializer(data= request.POST)
        if(flat_serializer.is_valid()):
            flat_serializer.save()
            return redirect(show)
            #return JsonResponse(flat_serializer.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in serializer",status=status.HTTP_404_NOT_FOUND)
    else:
        return HttpResponse("Get method is not allowed",status=status.HTTP_405_METHOD_NOT_ALLOWED)

@csrf_exempt
def view_details(request):
    if(request.method == "GET"):
        flat = Flatsmanage.objects.all()
        flat_serializer = FlatSerializer(flat,many=True)
        return JsonResponse(flat_serializer.data,safe=False,status=status.HTTP_200_OK)

@csrf_exempt
def view_single(request,fetchid):
    try:
        flat = Flatsmanage.objects.get(Building_no = fetchid)
    except Flatsmanage.DoesNotExist:
        return HttpResponse("Invalid building no",status=status.HTTP_404_NOT_FOUND)
    if(request.method == "GET"):
        flat_serializer = FlatSerializer(flat)
        return JsonResponse(flat_serializer.data,status=status.HTTP_200_OK)
    if(request.method == "PUT"):
        mydata = JSONParser().parse(request)
        flat_serializer = FlatSerializer(flat,data=mydata)
        if(flat_serializer.is_valid()):
            flat_serializer.save()
            return JsonResponse(flat_serializer.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in serializer",status=status.HTTP_404_NOT_FOUND)
    if(request.method == "DELETE"):
        flat.delete()
        return HttpResponse("Deleted item",status=status.HTTP_204_NO_CONTENT)

@csrf_exempt
def search(request):
    try:
        getBuilding_no = request.POST.get("Building_no")
        getflat = Flatsmanage.objects.filter(Building_no = getBuilding_no)
        flat_serializer = FlatSerializer(getflat,many=True)
        return render(request,'search_detail.html',{"data":flat_serializer.data})
    except Flatsmanage.DoesNotExist:
        return HttpResponse("Invalid no",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("something went wrong")

@csrf_exempt
def update(request):
    try:
        getBuilding_no = request.POST.get("Building_no")
        getflat = Flatsmanage.objects.filter(Building_no = getBuilding_no)
        flat_serializer = FlatSerializer(getflat,many=True)
        return render(request,'update_detail.html',{"data":flat_serializer.data})
    except Flatsmanage.DoesNotExist:
        return HttpResponse("Invalid no",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("something went wrong")

@csrf_exempt
def action_update(request):
    getnewId = request.POST.get("newId")
    getnewBuilding_no = request.POST.get("newBuilding_no")
    getnewOwner_name = request.POST.get("newOwner_name")
    getnewAddress = request.POST.get("newAddress")
    getnewMob_no = request.POST.get("newMob_no")
    getnewAdhar_no = request.POST.get("newAdhar_no")
    getnewemail_id = request.POST.get("newemail_id")
    getnewpassword = request.POST.get("newpassword")
    mydata = {"Building_no":getnewBuilding_no,"Owner_name":getnewOwner_name,"Address":getnewAddress,"Mob_no":getnewMob_no,"Adhar_no":getnewAdhar_no,
    "email_id":getnewemail_id,"password":getnewpassword}
    jsondata = json.dumps(mydata)
    APIlink = "http://127.0.0.1:8000/flat/view/"+getnewId
    requests.put(APIlink,data=jsondata)
    return HttpResponse("Updated successfully")

@csrf_exempt
def delete(request):
    try:
        getBuilding_no = request.POST.get("Building_no")
        getflat = Flatsmanage.objects.filter(Building_no = getBuilding_no)
        flat_serializer = FlatSerializer(getflat,many=True)
        return render(request,'delete_detail.html',{"data":flat_serializer.data})
    except Flatsmanage.DoesNotExist:
        return HttpResponse("Invalid no",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("Something went wrong")

@csrf_exempt
def action_delete(request):
    getnewId = request.POST.get("newId")
    APIlink = "http://127.0.0.1:8000/flat/view/"+getnewId
    requests.delete(APIlink)
    return HttpResponse("Deleted successfully")
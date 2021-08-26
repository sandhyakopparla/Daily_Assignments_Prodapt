import json
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from flats.serializers import FlatSerializer
from flats.models import Flatsapp
import requests

def homepage(request):
    return render(request,'home.html')

def addpage(request):
    return render(request,'add.html')

def viewpage(request):
    fetchdata=requests.get("http://127.0.0.1:8000/flats/view/").json()
    return render(request,'view.html',{"data":fetchdata})

def searchpage(request):
    return render(request,'search.html')

def updatepage(request):
    return render(request,'update.html')

def deletepage(request):
    return render(request,'delete.html')

@csrf_exempt
def flatadd(request):
    if(request.method=="POST"):
        Flat_Serializer=FlatSerializer(data=request.POST)
        if(Flat_Serializer.is_valid()):
            Flat_Serializer.save()
            return redirect(viewpage)

@csrf_exempt
def search(request):
    try:
        getbuildingno = request.POST.get("buildingno")
        getbuilding = Flatsapp.objects.filter(buildingno=getbuildingno)
        Flat_Serializer = FlatSerializer(getbuilding,many=True)
        return render(request,'search.html',{"data":Flat_Serializer.data})
    except Flatsapp.DoesNotExist:
        return HttpResponse('Invalid Building Number')
    except:
        return HttpResponse("Something went wrong")

@csrf_exempt
def apiupdate(request):
    try:
        getbuildingno = request.POST.get("buildingno")
        getbuilding = Flatsapp.objects.filter(buildingno=getbuildingno)
        Flat_Serializer = FlatSerializer(getbuilding,many=True)
        return render(request,'update.html',{"data":Flat_Serializer.data})
    except Flatsapp.DoesNotExist:
        return HttpResponse('Invalid Building Number')
    except:
        return HttpResponse("Something went wrong")

@csrf_exempt
def update(request):
    getbuildingno = request.POST.get("newbuildingno")
    getownername = request.POST.get("newownername")
    getaddress = request.POST.get("newaddress")
    getadhar = request.POST.get("newadhar")
    getmobile = request.POST.get("newmobile")
    getemail = request.POST.get("newemail")
    getpassword = request.POST.get("newpassword")
    mydata = {"buildingno":getbuildingno,"ownername":getownername,"address":getaddress,"adhar":getadhar,"mobile":getmobile,"email":getemail,"password":getpassword}
    jsondata = json.dumps(mydata)
    print(jsondata)
    Apilink = "http://127.0.0.1:8000/flats/all/"+str(getbuildingno)
    requests.put(Apilink, data=jsondata)
    return redirect(viewpage)

@csrf_exempt
def delete(request):
    getbuildingno = request.POST.get("newbuildingno")
    Apilink = "http://127.0.0.1:8000/flats/all/"+str(getbuildingno)
    requests.delete(Apilink)
    return redirect(viewpage)

@csrf_exempt
def apidelete(request):
    try:
        getbuildingno = request.POST.get("buildingno")
        getbuilding = Flatsapp.objects.filter(buildingno=getbuildingno)
        Flat_Serializer = FlatSerializer(getbuilding,many=True)
        return render(request,'delete.html',{"data":Flat_Serializer.data})
    except Flatsapp.DoesNotExist:
        return HttpResponse('Invalid Building Number')
    except:
        return HttpResponse("Something went wrong")





      
@csrf_exempt
def flat_list(request):
    if(request.method=="GET"):
        flats=Flatsapp.objects.all()
        Flat_Serializer=FlatSerializer(flats, many=True)
        return JsonResponse(Flat_Serializer.data, safe=False)

@csrf_exempt
def flatdetail(request,id):
    try:
        flats=Flatsapp.objects.get(buildingno=id)
        if(request.method == "GET"):
            Flat_Serializer=FlatSerializer(flats)
            return JsonResponse(Flat_Serializer.data,safe=False,status=status.HTTP_200_OK)
        if(request.method=="DELETE"):
            flats.delete()
            return HttpResponse("deleted",status=status.HTTP_204_NO_CONTENT)
        if(request.method == "PUT"):
            mydata=JSONParser().parse(request)
            Flat_Serializer = FlatSerializer(flats,data=mydata)
            if(Flat_Serializer.is_valid()):
                Flat_Serializer.save()
                return JsonResponse(Flat_Serializer.data,status=status.HTTP_200_OK)

            else:
                return HttpResponse("Error in serializers")
    except Flatsapp.DoesNotExist:
        return HttpResponse("Invalid Building no",status=status.HTTP_404_NOT_FOUND)
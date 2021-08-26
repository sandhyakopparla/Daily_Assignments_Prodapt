from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework.parsers import JSONParser
from flats.models import Flat
from flats.serializers import flatSerializer
import requests
from rest_framework import status



def addflat(request):
    return render(request,"add.html")

def searchflat(request):
    return render(request,"search.html")


def veiwallflats(request):
    fetchdata=requests.get("http://127.0.0.1:8000/flats/viewall/").json()
    return render(request,"viewall.html",{"data":fetchdata})

def updateflats(request):
    return render(request,"update.html")

def deleteflats(request):
    return render(request,"delete.html")


@csrf_exempt
def flat(request):
    if(request.method=="POST"):
        # mydata=JSONParser().parse(request)
        flat_serialize=flatSerializer(data=request.POST)
        if(flat_serialize.is_valid()):
            flat_serialize.save()
            return JsonResponse(flat_serialize.data)
        else:
            return HttpResponse("error in serialization")

    else:
        return HttpResponse("sucess")

@csrf_exempt
def flat_list(request):
    if(request.method=="GET"):
        flats=Flat.objects.all()
        flat_serializer=flatSerializer(flats,many=True)
        return JsonResponse(flat_serializer.data,safe=False)


@csrf_exempt
def myflats(request,fetchid):
    try:
        flat1=Flat.objects.get(id=fetchid)
        if(request.method=="GET"):
            flat_serializer=flatSerializer(flat1)
            return JsonResponse(flat_serializer.data,safe=False)

        if(request.method=="DELETE"):
            flat1.delete()
            return HttpResponse("Deleted",status=status)

        if(request.method=="PUT"):
            flatdata=JSONParser().parse(request)
            flat_serialize=flatSerializer(flat1,data=flatdata)
            if (flat_serialize.is_valid()):
                flat_serialize.save()
                return JsonResponse(flat_serialize.data)
            else:
                return JsonResponse(flat_serialize.errors)
    except Flat.DoesNotExist:
        return HttpResponse("invalid syntax")


@csrf_exempt
def searchapi(request):
    try:
        getbno=request.POST.get("buildingno")
        getflat=Flat.objects.filter(buildingno=getbno)
        flat_serializer=flatSerializer(getflat,many=True)
        return render(request,"search.html",{"data":flat_serializer.data})
        # return JsonResponse(flat_serializer.data,safe=False,status=status.HTTP_200_OK)
    except Flat.DoesNotExist:
        return HttpResponse("Invalid number",status=status.HTTP_404_NOT_FOUND)    
    
    except:
        return HttpResponse("something went wrong")


@csrf_exempt
def updateapi(request):
    try:
        getbno=request.POST.get("buildingno")
        getflat=Flat.objects.filter(buildingno=getbno)
        flat_serializer=flatSerializer(getflat,many=True)
        return render(request,"update.html",{"data":flat_serializer.data})
        # return JsonResponse(event_serializer.data,safe=False,status=status.HTTP_200_OK)
    except Flat.DoesNotExist:
        return HttpResponse("Invalid number",status=status.HTTP_404_NOT_FOUND)    
    
    except:
        return HttpResponse("something went wrong")


@csrf_exempt
def update_data(request):
    getnewid=request.POST.get("newid")

    getnewbuildingno=request.POST.get("newbuildingno")
    getnewownername=request.POST.get("newownername")
    getnewaddress=request.POST.get("newaddress")
    getnewmobileno=request.POST.get("newmobileno")
    getnewemail=request.POST.get("newemail")
    getnewadharno=request.POST.get("newadharno")
    getnewpassword=request.POST.get("newpassword")

    mydata={'buildingno': getnewbuildingno,'ownername':getnewownername,'address':getnewaddress,'mobileno':getnewmobileno,'email':getnewemail,'adharno':getnewadharno,'password':getnewpassword}
    jsondata=json.dumps(mydata)
    Apilink="http://127.0.0.1:8000/flats/view/"+getnewid
    requests.put(Apilink,data=jsondata)
    return HttpResponse("data has updated sucessfully")


@csrf_exempt
def deleteapi(request):
    try:
        getbno=request.POST.get("buildingno")
        getflat=Flat.objects.filter(buildingno=getbno)
        flat_serializer=flatSerializer(getflat,many=True)
        return render(request,"delete.html",{"data":flat_serializer.data})
        # return JsonResponse(event_serializer.data,safe=False,status=status.HTTP_200_OK)
    except Event.DoesNotExist:
        return HttpResponse("Invalid number",status=status.HTTP_404_NOT_FOUND)    
    
    except:
        return HttpResponse("something went wrong")


@csrf_exempt
def delete_data(request):
    getnewid=request.POST.get("newid")
    Apilink="http://127.0.0.1:8000/flats/view/"+getnewid
    requests.delete(Apilink)
    return HttpResponse("data has deleted sucessfully")

from flat.models import Flat
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from flat.serializers import FlatSerializer
from rest_framework.parsers import JSONParser
from rest_framework import status
import requests



# Create your views here.
@csrf_exempt
def DeleteRead(request):
    getNewId=request.POST.get("newid")
    ApiLink="http://127.0.0.1:8000/flat/viewflat/" + getNewId
    requests.delete(ApiLink)
    return redirect(myViewAllPage)

@csrf_exempt
def DeleteSearchAPI(request):
    try:
        getBuildingno=request.POST.get("building_no")
        getOwnername=Flat.objects.filter(building_no=getBuildingno)
        flat_serializer=FlatSerializer(getOwnername,many=True)
        return render(request,"delete.html",{"data":flat_serializer.data})
        #return JsonResponse(flat_serializer.data,safe=False,status=status.HTTP_200_OK)
    except Flat.DoesNotExist:
        return HttpResponse("Invalid",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("Something Wrong")


@csrf_exempt
def UpdateRead(request):
    getNewId=request.POST.get("newid")
    getNewbuildingno=request.POST.get("newbuildingno")
    getNewownername=request.POST.get("newownername")
    getNewaddress=request.POST.get("newaddress")
    getNewmblno=request.POST.get("newmblno")
    getNewaadharno=request.POST.get("newaadharno")
    getNewemailid=request.POST.get("newemailid")
    getNewpassword=request.POST.get("newpassword")
    mydata={'building_no':getNewbuildingno,'owner_name':getNewownername,'address':getNewaddress,'mbl_no':getNewmblno,'aadhar_no':getNewaadharno,'email_id':getNewemailid,'password':getNewpassword}
    jsondata=json.dumps(mydata)
    ApiLink="http://127.0.0.1:8000/flat/viewflat/" + getNewId
    print(jsondata)
    requests.put(ApiLink,data=jsondata)
    return redirect(myViewAllPage)
    #return HttpResponse("Data Updated Successfully!!!")


@csrf_exempt
def UpdateSearchAPI(request):
    try:
        getBuildingno=request.POST.get("building_no")
        getOwnername=Flat.objects.filter(building_no=getBuildingno)
        flat_serializer=FlatSerializer(getOwnername,many=True)
        return render(request,"update.html",{"data":flat_serializer.data})
        #return JsonResponse(flat_serializer.data,safe=False,status=status.HTTP_200_OK)
    except Flat.DoesNotExist:
        return HttpResponse("Invalid",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("Something Wrong")

@csrf_exempt
def SearchAPI(request):
    try:
        getBuildingno=request.POST.get("building_no")
        getOwnername=Flat.objects.filter(building_no=getBuildingno)
        flat_serializer=FlatSerializer(getOwnername,many=True)
        return render(request,"search.html",{"data":flat_serializer.data})
        #return JsonResponse(flat_serializer.data,safe=False,status=status.HTTP_200_OK)
    except Flat.DoesNotExist:
        return HttpResponse("Invalid",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("Something Went Wrong")

def myFlat(request):
    return render(request,'flat.html')

def myDelete(request):
    return render(request,'delete.html')

def myUpdate(request):
    return render(request,'update.html')

def myWelcomePage(request):
    return render(request,'welcome.html')


def myViewAllPage(request):
    fetchdata=requests.get("http://127.0.0.1:8000/flat/viewall/").json()
    return render(request,'viewall.html',{"data":fetchdata})

def mySearch(request):
    return render(request,'search.html')


@csrf_exempt
def myFlatDetails(request,id):
    try:
        flats=Flat.objects.get(id=id)
        if (request.method=="GET"):    
            flat_serializer=FlatSerializer(flats)
            return JsonResponse(flat_serializer.data,safe=False,status=status.HTTP_200_OK)
        if (request.method=="DELETE"):  
            flats.delete()
            return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)
        if (request.method=="PUT"):  
            dict=JSONParser().parse(request)
            flat_serialize=FlatSerializer(flats,data=dict)
            if(flat_serialize.is_valid()):
                flat_serialize.save()
                return JsonResponse(flat_serialize.data,status=status.HTTP_200_OK)
            else:
                return JsonResponse(flat_serialize.errors,status=status.HTTP_400_BAD_REQUEST)
    except Flat.DoesNotExist:
        return HttpResponse("Invalid",status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
def myFlatList(request):
    if(request.method=="GET"):
        flats=Flat.objects.all()
        flat_serializer=FlatSerializer(flats,many=True)
        return JsonResponse(flat_serializer.data,safe=False)

@csrf_exempt
def myFlatPage(request):
    if(request.method=="POST"):
        #dict=JSONParser().parse(request)
        flat_serialize=FlatSerializer(data=request.POST)
        if(flat_serialize.is_valid()):
            flat_serialize.save()
            return redirect(myViewAllPage)
            # return JsonResponse(flat_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in Serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("GET Method Not Allowed",status=status.HTTP_404_NOT_FOUND)
        
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from flats.serializers import FlatSerializer
from flats.models import Flat
from rest_framework.parsers import JSONParser
import requests,json
from django.shortcuts import redirect

# Create your views here.
@csrf_exempt
def addFlat(request):
    if(request.method=="POST"):
        #mydict=JSONParser().parse(request)
        flat_serialize=FlatSerializer(data=request.POST)
        if(flat_serialize.is_valid()):
            flat_serialize.save()
            return redirect(viewingFlat)
            #return JsonResponse(flat_serialize.data)
        else:
            return HttpResponse("error in serialization")
    else:
        return HttpResponse("GET method")

@csrf_exempt
def viewFlats(request):
    if(request.method=="GET"):
        flats=Flat.objects.all()
        flat_serialize=FlatSerializer(flats,many=True)
        return JsonResponse(flat_serialize.data,safe=False)


@csrf_exempt
def FlatDetails(request,building_no):
    try:
        flats=Flat.objects.get(building_no=building_no)
    except Flat.DoesNotExist:
        return HttpResponse("invalid Building_no")
    if(request.method=="GET"):
        flat_serialize=FlatSerializer(flats)
        return JsonResponse(flat_serialize.data,safe=False)
    if(request.method=="DELETE"):
        flats.delete()
        return HttpResponse("deleted")
    if(request.method=="PUT"):
        mydict=JSONParser().parse(request)
        flat_serialize=FlatSerializer(flats,data=mydict)
        if(flat_serialize.is_valid()):
            flat_serialize.save()
            return JsonResponse(flat_serialize.data)

def add_flat(request):
    return render(request,'register.html')

def viewingFlat(request):
    fetchdata=requests.get("http://127.0.0.1:8000/flats/viewall/").json()
    return render(request,'view.html',{"data":fetchdata})

def searchFlat(request):
    return render(request,'search.html')

def updateFlat(request):
    return render(request,'update.html')

def deleteFlat(request):
    return render(request,'delete.html')


@csrf_exempt
def searchapi(request):
    try:
        getBuilding_No=request.POST.get("building_no")
        get_Building=Flat.objects.filter(building_no=getBuilding_No)
        flat_serialize=FlatSerializer(get_Building,many=True)
        return render(request,"search.html",{"data":flat_serialize.data})
        #return JsonResponse(flat_serialize.data,safe=False)
    except Flat.DoesNotExist:
        return HttpResponse("Invalid Building_No")
    except:
        return HttpResponse("something went wrong")

@csrf_exempt
def update_api(request):
    try:
        getBuilding_No=request.POST.get("building_no")
        get_Building=Flat.objects.filter(building_no=getBuilding_No)
        flat_serialize=FlatSerializer(get_Building,many=True)
        return render(request,"update.html",{"data":flat_serialize.data})
        #return JsonResponse(flat_serialize.data,safe=False)
    except Flat.DoesNotExist:
        return HttpResponse("Invalid Building_No")
    except:
        return HttpResponse("something went wrong")


@csrf_exempt
def update_data_read(request):
    getNewId=request.POST.get("newId")
    getBuildingNo=request.POST.get("newbuilding_no")
    getOwnerName=request.POST.get("newowner_name")
    getAddress=request.POST.get("newaddress")
    getMobileNo=request.POST.get("newmobile_no")
    getAadharNo=request.POST.get("newaadhar_no")
    getEmailId=request.POST.get("newmail_id")
    getPassword=request.POST.get("newpassword")
    mydata={"building_no":getBuildingNo,"owner_name":getOwnerName,"address":getAddress,"mobile_no":getMobileNo,"aadhar_no":getAadharNo,"mail_id":getEmailId,"password":getPassword}
    jsondata=json.dumps(mydata)
    print(jsondata)
    ApiLink="http://127.0.0.1:8000/flats/view/"+getNewId
    requests.put(ApiLink,data=jsondata)
    return HttpResponse("Updated successfully")

@csrf_exempt
def delete_api(request):
    try:
        getBuilding_No=request.POST.get("building_no")
        get_Building=Flat.objects.filter(building_no=getBuilding_No)
        flat_serialize=FlatSerializer(get_Building,many=True)
        return render(request,"delete.html",{"data":flat_serialize.data})
        #return JsonResponse(flat_serialize.data,safe=False)
    except Flat.DoesNotExist:
        return HttpResponse("Invalid Building_No")
    except:
        return HttpResponse("something went wrong")


@csrf_exempt
def delete_data_read(request):
    getNewId=request.POST.get("newId")
    ApiLink="http://127.0.0.1:8000/flats/view/"+getNewId
    requests.delete(ApiLink)
    return HttpResponse("Deleted successfully")
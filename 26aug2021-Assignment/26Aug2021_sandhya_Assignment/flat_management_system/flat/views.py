from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse
import json
from flat.serializers import flatSerializer
from flat.models import Flat
from rest_framework.parsers import JSONParser 
from rest_framework import status
import requests
@csrf_exempt
def update_data_read(request):
    getId=request.POST.get("newid")
    getbuilding_no=request.POST.get("newbuildingnumber")
    getowner_name=request.POST.get("newownername")
    getmobile_no=request.POST.get("newmobilenumber")
    getaddress=request.POST.get("newaddress")
    getadharno=request.POST.get("newadharno")
    getemailid=request.POST.get("newemailid")
    getpassword=request.POST.get("newpassword") 
    mydata={"building_no":getbuilding_no,"owner_name":getowner_name,"mobile_no":getmobile_no,"address":getaddress,"adhar_no": getadharno,"emailId":getemailid,"password":getpassword}
    jsondata=json.dumps(mydata)
    ApiLink="http://localhost:8000/flat/viewflat/"+ getId
    requests.put(ApiLink,data=jsondata)
    return HttpResponse("data updated successfully")
@csrf_exempt 
def update_api(request):
    try:
        getbuilding_no=request.POST.get("building_no")
        getBuildings=Flat.objects.filter(building_no=getbuilding_no)
        flat_serializer=flatSerializer(getBuildings,many=True)
        return render(request,"update.html",{"data":flat_serializer.data})

    except:
        return HttpResponse("invalid building number")

@csrf_exempt
def searchapi(request):
    try:
        getbuilding_no=request.POST.get("building_no")
        getBuildings=Flat.objects.filter(building_no=getbuilding_no)
        flat_serializer=flatSerializer(getBuildings,many=True)
        return render(request,"search.html",{"data":flat_serializer.data})

    except:
        return HttpResponse("invalid building no")
@csrf_exempt
def delete_data_read(request):
    getId=request.POST.get("newid")
    ApiLink="http://localhost:8000/flat/viewflat/"+ getId 
    requests.delete(ApiLink)
    return HttpResponse("data deleted successfully")
@csrf_exempt
def delete_api(request):
    try:
        getbuilding_no=request.POST.get("building_no")
        getBuildings=Flat.objects.filter(building_no=getbuilding_no)
        flat_serializer=flatSerializer(getBuildings,many=True)
        return render(request,"delete.html",{"data":flat_serializer.data})
    except:
        return HttpResponse("invalid building number")
@csrf_exempt
def flatPage(request):
    if(request.method=="POST"):
    #    mydict=JSONParser().parse(request)   
       flat_serialize=flatSerializer(data=request.POST)  
       if(flat_serialize.is_valid()):
           flat_serialize.save()
           return redirect(viewall)
       else:
           return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("No Get method allowed",status=status.HTTP_400_BAD_REQUEST)
@csrf_exempt
def flat_list(request):
    if(request.method=="GET"):
        flat=Flat.objects.all()
        flat_serialize=flatSerializer(flat,many=True)
        return JsonResponse(flat_serialize.data,safe=False)
@csrf_exempt
def flat_details(request,fetchid):
    try:
        flat=Flat.objects.get(id=fetchid)
        if(request.method=="GET"):
            flat_serializer=flatSerializer(flat)
            return JsonResponse(flat_serializer.data,safe=False,status=status.HTTP_200_OK)
        if (request.method=="DELETE"):
            flat.delete()
            return HttpResponse("Deleted",status=status.HTTP_200_OK)
        if (request.method=="PUT"):
            mydict=JSONParser().parse(request)
            flat_serializer=flatSerializer(flat,data=mydict)
            if(flat_serializer.is_valid()):
                flat_serializer.save()
                return JsonResponse(flat_serializer.data,status=status.HTTP_200_OK)
            else:
                return JsonResponse(flat_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    except Flat.DoesNotExist:
        return HttpResponse("invalid flat no",status=status.HTTP_404_NOT_FOUND)

def flatregister_view(request):
    return render(request,'register.html')
def home_view(request):
    return render(request,'home.html')
def viewall(request):   #where is update data read  api
    fetchdata=requests.get("http://127.0.0.1:8000/flat/viewall/").json()
    return render(request,'viewflat.html',{"data":fetchdata})
def search_view(request):
    return render(request,'search.html')
def delete_view(request):
    return render(request,'delete.html')
def update_view(request):
    return render(request,'update.html')
def contact_view(request):
    return render(request,'contact.html')
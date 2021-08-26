from django.shortcuts import redirect,render
from flat.models import Flat
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from flat.serializers import FlatSerializer
from rest_framework.parsers import JSONParser
from rest_framework import status
import requests

# Create your views here.

def delete_flat_view(request):
    return render(request,'delete.html')
@csrf_exempt
def delete_data_read(request):
    getnewid=request.POST.get("newid")
    # getnewbuildingno=request.POST.get("newbuildingno")
    # getnewownername=request.POST.get("newownername")
    # getnewaddress=request.POST.get("newaddress")
    # getnewmobileno=request.POST.get("newmobileno")
    # getnewadhaarno=request.POST.get("newadhaarno")
    # getnewemailid=request.POST.get("newemailid")
    # getnewpassword=request.POST.get("newpassword")
    # mydata={'buildingno':getnewbuildingno,'ownername':getnewownername,'address':getnewaddress,'mobileno':getnewmobileno,
    #         'adhaarno ':getnewadhaarno,'emailid':getnewemailid,'password':getnewpassword}
    # jsondata=json.dumps(mydata)
    # print(jsondata)
    Apilink="http://127.0.0.1:8000/flat/view/"+getnewid
    requests.delete(Apilink)
    return HttpResponse("Data has deleted succesfully")
@csrf_exempt
def deleteapi(request):
    try:
        getbulidingno=request.POST.get("buildingno")
        getflat=Flat.objects.filter(buildingno=getbulidingno)
        flat_serializer=FlatSerializer(getflat,many=True)
        print(flat_serializer.data)
        # return JsonResponse(flat_serializer.data,safe=False,status=status.HTTP_200_OK)
        return render(request,"delete.html",{"data":flat_serializer.data})
    except Flat.DoesNotExist:
        return HttpResponse("Invalid buildingno",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("Something Went Wrong")
        
def update_flat_view(request):
    return render(request,'update.html')
@csrf_exempt
def updateapi(request):
    try:
        getbulidingno=request.POST.get("buildingno")
        getflat=Flat.objects.filter(buildingno=getbulidingno)
        flat_serializer=FlatSerializer(getflat,many=True)
        print(flat_serializer.data)
        # return JsonResponse(flat_serializer.data,safe=False,status=status.HTTP_200_OK)
        return render(request,"update.html",{"data":flat_serializer.data})
    except Flat.DoesNotExist:
        return HttpResponse("Invalid buildingno",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("Something Went Wrong")
@csrf_exempt
def update_data_read(request):
    getnewid=request.POST.get("newid")
    getnewbuildingno=request.POST.get("newbuildingno")
    getnewownername=request.POST.get("newownername")
    getnewaddress=request.POST.get("newaddress")
    getnewmobileno=request.POST.get("newmobileno")
    getnewadhaarno=request.POST.get("newadhaarno")
    getnewemailid=request.POST.get("newemailid")
    getnewpassword=request.POST.get("newpassword")
    mydata={'buildingno':getnewbuildingno,'ownername':getnewownername,'address':getnewaddress,'mobileno':getnewmobileno,
            'adhaarno ':getnewadhaarno,'emailid':getnewemailid,'password':getnewpassword}
    jsondata=json.dumps(mydata)
    print(jsondata)
    Apilink="http://127.0.0.1:8000/flat/view/"+getnewid
    requests.put(Apilink,data=jsondata)
    return HttpResponse("Data has updated succesfully")
def search_flat_view(request):
    return render(request,'search.html')
@csrf_exempt
def searchapi(request):
    try:
        getbulidingno=request.POST.get("buildingno")
        getflat=Flat.objects.filter(buildingno=getbulidingno)
        flat_serializer=FlatSerializer(getflat,many=True)
        print(flat_serializer.data)
        # return JsonResponse(flat_serializer.data,safe=False,status=status.HTTP_200_OK)
        return render(request,"search.html",{"data":flat_serializer.data})
    except Flat.DoesNotExist:
        return HttpResponse("Invalid buildingno",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("Something Went Wrong")
def viewall_flat_view(request):
    fetchdata=requests.get("http://127.0.0.1:8000/flat/viewall/").json()
    return render(request,'viewall.html',{"data":fetchdata})
def add_flat_view(request):
    return render(request,'sub.html')
@csrf_exempt
def flat_list(request):
    if(request.method=="GET"):
        flat=Flat.objects.all()
        flat_serializer=FlatSerializer(flat,many=True)
        return JsonResponse(flat_serializer.data,safe=False)
@csrf_exempt
def flat_create(request):
    if(request.method=="POST"):
        # mydata=JSONParser().parse(request)
        flat_serialize=FlatSerializer(data=request.POST)
        if(flat_serialize.is_valid()):
            flat_serialize.save()
            return redirect(viewall_flat_view)
        else:
            return HttpResponse("Error in Serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("Get Method Not Allowed",status=status.HTTP_404_NOT_FOUND)
@csrf_exempt
def flat_details(request,id):
    try:
        flats=Flat.objects.get(id=id)
        if(request.method=="GET"):
            flat_serializer=FlatSerializer(flats)
            return JsonResponse(flat_serializer.data,safe=False,status=status.HTTP_200_OK)
        if(request.method=="DELETE"):
            flats.delete()
            return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)
        if(request.method=="PUT"):
            mydata=JSONParser().parse(request)
            flat_serialize=FlatSerializer(flats,data=mydata)
            if(flat_serialize.is_valid()):
                flat_serialize.save()
                return JsonResponse(flat_serialize.data,status=status.HTTP_200_OK)
            else:
                return JsonResponse(flat_serialize.errors,status=status.HTTP_400_BAD_REQUEST)
    except Flat.DoesNotExist:
        return HttpResponse("Invalid Id",status=status.HTTP_404_NOT_FOUND)

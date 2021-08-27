from re import search
from django.shortcuts import render
from django.http.response import HttpResponse,JsonResponse
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
import requests
from flats.models import Flats
from flats.serializers import FlatsSerializer
from rest_framework import status
import json
# Create your views here.

def home(request):
    return render(request,'home.html')

def add_page(request):
    return render(request,'add.html')

def view_page(request):
    flatdata = requests.get("http://127.0.0.1:8000/flats/all/").json()
    return render(request,"view.html",{'data':flatdata})

def search_page(request):
    return render(request,'search.html')

def update_page(request):
    return render(request,'update.html')

def delete_page(request):
    return render(request,'delete.html')

@csrf_exempt
def add_flat(request):
    if(request.method == "POST"):
        # flat= JSONParser().parse(request)
        flat_serialize = FlatsSerializer(data=request.POST)
        if(flat_serialize.is_valid()):
            flat_serialize.save()
            # return JsonResponse(flat_serialize.data)
            return redirect(view_page)
    #     else:
    #         return HttpResponse("error ")
    # else:
    #     return HttpResponse("no get method")


@csrf_exempt
def view_flat(request):
    if(request.method == "GET"):
        flat = Flats.objects.all()
        flat_serialize = FlatsSerializer(flat,many =True)
        return JsonResponse(flat_serialize.data,safe=False,status=status.HTTP_200_OK)


@csrf_exempt
def update(request,bulding_no):
    try:
        flat = Flats.objects.get(bulding_no=bulding_no)
        if(request.method == "GET"):
            flat_serialize = FlatsSerializer(flat)
            return JsonResponse(flat_serialize.data,status=status.HTTP_200_OK)

        if (request.method == "DELETE"):
            flat.delete()
            return HttpResponse("deleted")

        if(request.method == "PUT"):
            myflat = JSONParser().parse(request)
            flat_serialize = FlatsSerializer(flat,data=myflat)
            if(flat_serialize.is_valid()):
                flat_serialize.save()
                return JsonResponse(flat_serialize.data,status=status.HTTP_200_OK)
            
    except Flats.DoesNotExist:
        return HttpResponse("You Enter Invalid ID",status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
def search_flat(request):
    try:
        getbulding_no = request.POST.get("bulding_no")
        getbulding = Flats.objects.filter(bulding_no=getbulding_no)
        bulding_serialize = FlatsSerializer(getbulding,many=True)
        return render(request,'search.html',{"data":bulding_serialize.data})
    except Flats.DoesNotExist:
        return HttpResponse('Invalid prodeuct name ')
    except:
        return HttpResponse("something went wrong")


@csrf_exempt
def updateapi(request):
    try:
        getbulding_no = request.POST.get("bulding_no")
        getbulding = Flats.objects.filter(bulding_no=getbulding_no)
        bulding_serialize = FlatsSerializer(getbulding,many=True)
        return render(request,'update.html',{"data":bulding_serialize.data})
    except Flats.DoesNotExist:
        return HttpResponse('Invalid prodeuct name ')
    except:
        return HttpResponse("something went wrong")

@csrf_exempt
def update_flat(request):
    getid = request.POST.get("newid")
    getbuilding_no = request.POST.get("newbuilding_no")
    getownername = request.POST.get("newowner_name")
    getaddress = request.POST.get("newaddress")
    getmobile_no = request.POST.get("newmobile_no")
    getadhar_no = request.POST.get("newadhar_no")
    getemailid = request.POST.get("newemailid")
    getpassword = request.POST.get("newpassword")
    mydata= {"id":getid,"bulding_no":getbuilding_no,"owner_name":getownername,"address":getaddress,"mobile_no":getmobile_no,"adhar_no":getadhar_no,"emailid":getemailid,"password":getpassword}
    jsondata=json.dumps(mydata)
    # print(jsondata)
    apilink = "http://127.0.0.1:8000/flats/update/"+str(getbuilding_no)
    requests.put(apilink, data=jsondata)
    return redirect(view_page)

    # return HttpResponse('Data has updated successfully')

@csrf_exempt
def deleteapi(request):
    try:
        getflat = request.POST.get("bulding_no")
        getf = Flats.objects.filter(bulding_no=getflat)
        flat_serialize = FlatsSerializer(getf,many=True)
        return render(request,'delete.html',{"data":flat_serialize.data})
    except Flats.DoesNotExist:
        return HttpResponse('Invalid prodeuct name ')
    except:
        return HttpResponse("something went wrong")



@csrf_exempt
def delete_data(request): 
    getno = request.POST.get("newbuilding_no")
    apilink = "http://127.0.0.1:8000/flats/update/"+str(getno)
    requests.delete(apilink)
    # return HttpResponse('Data has deleted successfully')
    return redirect(view_page)
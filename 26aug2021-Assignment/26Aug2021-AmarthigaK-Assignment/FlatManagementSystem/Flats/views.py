from django.shortcuts import redirect, render

from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.http import HttpResponse
from django.http.response import JsonResponse

from Flats.models import flat
from Flats.serializer import flatSerializer
# Create your views here.

@csrf_exempt
def add(request):
    if(request.method =='POST'):
        #faltdata = JSONParser().parse(request)
        flat_serialize = flatSerializer(data=request.POST)

        if(flat_serialize.is_valid()):
            flat_serialize.save()
            #return JsonResponse(flat_serialize.data, status = status.HTTP_200_OK)
            return redirect(user)

        else:
            return HttpResponse("Error in Serialization", status = status.HTTP_400_BAD_REQUEST)

    else:
        return HttpResponse("Welcome")

@csrf_exempt
def viewall(request):
    if(request.method =='GET'):
        flats = flat.objects.all()
        flat_serializer = flatSerializer(flats, many=True)
        return JsonResponse(flat_serializer.data, safe=False)

    else:
        return HttpResponse("Welcome to view all")

@csrf_exempt
def updel(request, id):
    try:
        fal = flat.objects.get(id=id)
        if(request.method == 'GET'):
            fal_serializer = flatSerializer(fal)
            return JsonResponse(fal_serializer.data, safe=False, status = status.HTTP_200_OK)

        if (request.method =='DELETE'):
            fal.delete()
            return JsonResponse("Content has been deleted ",safe=False, status = status.HTTP_204_NO_CONTENT)

        if (request.method == 'PUT'):
            faldata = JSONParser().parse(request)
            fal_serializer = flatSerializer(fal, data=faldata)
            if(fal_serializer.is_valid()):
                fal_serializer.save()
                return JsonResponse(fal_serializer.data, status = status.HTTP_200_OK)

    except flat.DoesNotExist:
        return HttpResponse("Invalid", status = status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def search(request):
    try:
        getid = request.POST.get("id")
        getdetails = flat.objects.filter(id = getid)
        details_serial = flatSerializer(getdetails, many=True)
        return render(request, 'search.html',{"data":details_serial})

    except:
        return HttpResponse("Invalid")


def home(request):
    return render(request, 'home.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def signup(request):
    return render(request, 'add.html')

def search(request):
    return render(request, 'search.html')

def user(request):
    return render(request, 'userpage.html')

def login(request):
    return render(request, 'login.html')



    



    


from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from villamanage.serializer import VillaSerializer
from villamanage.models import Villa
from rest_framework.parsers import JSONParser
from rest_framework import status
# Create your views here.
def first(request):
    return render(request,'first.html')
def reg(request):
    return render(request,'register.html')
def wel(request):
    return render(request,'welcome.html')
def normal(request):
    return render(request,'normal.html')
def premium(request):
    return render(request,'premium.html')

@csrf_exempt
def add(request):
    if(request.method == "POST"):
        #mydata = JSONParser().parse(request)
        #villa_Serializer = VillaSerializer(data=mydata)
        villa_Serializer = VillaSerializer(data=request.POST)
        if(villa_Serializer.is_valid()):
            villa_Serializer.save()
            #return JsonResponse(villa_Serializer.data)
            return redirect(wel)
        else:
            return HttpResponse("Error in serializer",status=status.HTTP_404_NOT_FOUND)
    else:
        return HttpResponse("Get method is not allowed",status=status.HTTP_405_METHOD_NOT_ALLOWED)

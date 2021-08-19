from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse
import json
from seller.serializers import sellerSerializer
from seller.models import Seller
from rest_framework.parsers import JSONParser 
from rest_framework import status
@csrf_exempt
def sellerPage(request):
    if(request.method=="POST"):
       mydict=JSONParser().parse(request)   
       seller_serialize=sellerSerializer(data=mydict)  
       if(seller_serialize.is_valid()):
           seller_serialize.save()
           return JsonResponse(seller_serialize.data,status=status.HTTP_200_OK)
       else:
           return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return Httpresponse("No Get method allowed",status=status.HTTP_400_BAD-REQUEST)
@csrf_exempt
def seller_list(request):
    if(request.method=="GET"):
        seller=Seller.objects.all()
        seller_serializer=sellerSerializer(seller,many=True)
        return JsonResponse(seller_serializer.data,safe=False)
@csrf_exempt
def seller_details(request,fetchid):
    try:
        seller=Seller.objects.get(id=fetchid)
        if(request.method=="GET"):
            seller_serializer=sellerSerializer(seller)
            return JsonResponse(seller_serializer.data,safe=False,status=status.HTTP_200_OK)
        if (request.method=="DELETE"):
            seller.delete()
            return HttpResponse("Deleted",status=status.HTTP_200_OK)
        if (request.method=="PUT"):
            mydict=JSONParser().parse(request)
            seller_serializer=sellerSerializer(seller,data=mydict)
            if(seller_serializer.is_valid()):
                seller_serializer.save()
                return JsonResponse(seller_serializer.data,status=status.HTTP_200_OK)
            else:
                return JsonResponse(seller_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    except Seller.DoesNotExist:
        return HttpResponse("invalid seller Id",status=status.HTTP_404_NOT_FOUND)

def seller_view(request):
    return render(request,'indexed.html')
# Create your views here.

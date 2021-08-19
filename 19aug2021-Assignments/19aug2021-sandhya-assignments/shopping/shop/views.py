from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse
import json
from shop.serializers import shopSerializer
from shop.models import Shop
from rest_framework.parsers import JSONParser 
from rest_framework import status
@csrf_exempt
def shopPage(request):
    if(request.method=="POST"):
       mydict=JSONParser().parse(request)   
       shop_serialize=shopSerializer(data=mydict)  
       if(shop_serialize.is_valid()):
           shop_serialize.save()
           return JsonResponse(shop_serialize.data,status=status.HTTP_200_OK)
       else:
           return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return Httpresponse("No Get method allowed",status=status.HTTP_400_BAD-REQUEST)
@csrf_exempt
def shop_list(request):
    if(request.method=="GET"):
        shop=Shop.objects.all()
        shop_serializer=shopSerializer(shop,many=True)
        return JsonResponse(shop_serializer.data,safe=False)
@csrf_exempt
def shop_details(request,fetchid):
    try:
        shop=Shop.objects.get(id=fetchid)
        if(request.method=="GET"):
            shop_serializer=shopSerializer(shop)
            return JsonResponse(shop_serializer.data,safe=False,status=status.HTTP_200_OK)
        if (request.method=="DELETE"):
            shop.delete()
            return HttpResponse("Deleted",status=status.HTTP_200_OK)
        if (request.method=="PUT"):
            mydict=JSONParser().parse(request)
            shop_serializer=shopSerializer(shop,data=mydict)
            if(shop_serializer.is_valid()):
                shop_serializer.save()
                return JsonResponse(shop_serializer.data,status=status.HTTP_200_OK)
            else:
                return JsonResponse(shop_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    except Shop.DoesNotExist:
        return HttpResponse("invalid shop Id",status=status.HTTP_404_NOT_FOUND)

def shop_view(request):
    return render(request,'index.html')
# Create your views here.

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse
import json
from products.serializers import ProductSerializer
from products.models import Product
from rest_framework.parsers import JSONParser 
from rest_framework import status 

def product_view(request):
    return render(request,'indexing.html') 
# Create your views here.
@csrf_exempt
def productPage(request):
    if(request.method=="POST"):
       mydict=JSONParser().parse(request)   
       products_serialize=ProductSerializer(data=mydict)  
       if(products_serialize.is_valid()):
           products_serialize.save()
           return JsonResponse(products_serialize.data,status=status.HTTP_200_OK)
       else:
           return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return Httpresponse("No Get method allowed",status=status.HTTP_400_BAD-REQUEST)
@csrf_exempt
def product_list(request):
    if(request.method=="GET"):
        products=Product.objects.all()
        products_serializer=ProductSerializer(products,many=True)
        return JsonResponse(products_serializer.data,safe=False)
@csrf_exempt
def product_details(request,fetchid):  
    try:
        products=Product.objects.get(id=fetchid)
        if(request.method=="GET"):
            products_serializer=ProductSerializer(products)
            return JsonResponse(products_serializer.data,safe=False,status=status.HTTP_200_OK)
        if (request.method=="DELETE"):
            products.delete()
            return HttpResponse("Deleted",status=status.HTTP_200_OK)
        if (request.method=="PUT"):
            mydict=JSONParser().parse(request)
            products_serializer=ProductSerializer(products,data=mydict)
            if(products_serializer.is_valid()):
                products_serializer.save()
                return JsonResponse(products_serializer.data,status=status.HTTP_200_OK)
            else:
                return JsonResponse(products_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    except Product.DoesNotExist:
        return HttpResponse("invalid product Id",status=status.HTTP_404_NOT_FOUND)

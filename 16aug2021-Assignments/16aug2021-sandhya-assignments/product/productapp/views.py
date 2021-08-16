from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse
import json
from productapp.serializers import ProductSerializer
from productapp.models import Product
@csrf_exempt
def product_list(request):
    if(request.method=="GET"):
        products=Product.objects.all()
        product_serializer=ProductSerializer(products,many=True)
        return JsonResponse(product_serializer.data,safe=False)
@csrf_exempt
def productPage(request):
    if(request.method=="POST"):
        getCode=request.POST.get("code")
        getName=request.POST.get("name")
        getDescription=request.POST.get("description")
        getPrice=request.POST.get("price")
        mydict={"code":getCode,"name":getName,"description":getDescription,"price":getPrice}
        product_serialize=ProductSerializer(data=mydict)
        if(product_serialize.is_valid()):
            product_serialize.save()
            return JsonResponse(product_serialize.data)
        else:
            return HttpResponse("error in serialization")
    else:
        return HttpResponse("No get method allowed")
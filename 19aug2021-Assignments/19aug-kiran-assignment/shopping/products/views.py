from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from products.serializers import ProductSerializer
from products.models import Product
from rest_framework.parsers import JSONParser
# Create your views here.
def add_product(request):
    return render(request,'int.html')


@csrf_exempt
def productDetails(request,fetchid):
    try:
        products=Product.objects.get(id=fetchid)
    except Product.DoesNotExist:
        return HttpResponse("invalid product ID")
    if(request.method=="GET"):
        product_serialize=ProductSerializer(products)
        return JsonResponse(product_serialize.data,safe=False)
    if(request.method=="DELETE"):
        products.delete()
        return HttpResponse("deleted")
    if(request.method=="PUT"):
        mydict=JSONParser().parse(request)
        product_serialize=ProductSerializer(products,data=mydict)
        if(product_serialize.is_valid()):
            product_serialize.save()
            return JsonResponse(product_serialize.data)


@csrf_exempt
def viewproduct(request):
    if(request.method=="GET"):
        products=Product.objects.all()
        product_serialize=ProductSerializer(products,many=True)
        return JsonResponse(product_serialize.data,safe=False)

@csrf_exempt
def addproduct(request):
    if(request.method=="POST"):
        mydict=JSONParser().parse(request)
        product_serialize=ProductSerializer(data=mydict)
        if(product_serialize.is_valid()):
            product_serialize.save()
            return JsonResponse(product_serialize.data)
        else:
            return HttpResponse("error in serialization")
    else:
        return HttpResponse("GET method")
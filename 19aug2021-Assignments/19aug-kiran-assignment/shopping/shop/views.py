from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from shop.serializers import ShopSerializer
from shop.models import Shop
from rest_framework.parsers import JSONParser

# Create your views here.
def add_page(request):
    return render(request,'index.html')

@csrf_exempt
def shopDetails(request,fetchid):
    try:
        shops=Shop.objects.get(id=fetchid)
    except Shop.DoesNotExist:
        return HttpResponse("invalid shop ID")
    if(request.method=="GET"):
        shop_serialize=ShopSerializer(shops)
        return JsonResponse(shop_serialize.data,safe=False)
    if(request.method=="DELETE"):
        shops.delete()
        return HttpResponse("deleted")
    if(request.method=="PUT"):
        mydict=JSONParser().parse(request)
        shop_serialize=ShopSerializer(shops,data=mydict)
        if(shop_serialize.is_valid()):
            shop_serialize.save()
            return JsonResponse(shop_serialize.data)


@csrf_exempt
def viewShop(request):
    if(request.method=="GET"):
        shops=Shop.objects.all()
        shop_serialize=ShopSerializer(shops,many=True)
        return JsonResponse(shop_serialize.data,safe=False)

@csrf_exempt
def addShop(request):
    if(request.method=="POST"):
        mydict=JSONParser().parse(request)
        shop_serialize=ShopSerializer(data=mydict)
        if(shop_serialize.is_valid()):
            shop_serialize.save()
            return JsonResponse(shop_serialize.data)
        else:
            return HttpResponse("error in serialization")
    else:
        return HttpResponse("GET method")
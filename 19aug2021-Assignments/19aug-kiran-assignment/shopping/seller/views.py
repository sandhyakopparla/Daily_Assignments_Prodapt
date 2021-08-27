from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from seller.serializers import SellerSerializer
from seller.models import Seller
from rest_framework.parsers import JSONParser
# Create your views here.
def add_seller(request):
    return render(request,'text.html')


@csrf_exempt
def sellerDetails(request,fetchid):
    try:
        sellers=Seller.objects.get(id=fetchid)
    except Seller.DoesNotExist:
        return HttpResponse("invalid seller ID")
    if(request.method=="GET"):
        seller_serialize=SellerSerializer(sellers)
        return JsonResponse(seller_serialize.data,safe=False)
    if(request.method=="DELETE"):
        sellers.delete()
        return HttpResponse("deleted")
    if(request.method=="PUT"):
        mydict=JSONParser().parse(request)
        seller_serialize=SellerSerializer(sellers,data=mydict)
        if(seller_serialize.is_valid()):
            seller_serialize.save()
            return JsonResponse(seller_serialize.data)
      

@csrf_exempt
def viewseller(request):
    if(request.method=="GET"):
        sellers=Seller.objects.all()
        seller_serialize=SellerSerializer(sellers,many=True)
        return JsonResponse(seller_serialize.data,safe=False)



@csrf_exempt
def addseller(request):
    if(request.method=="POST"):
        mydict=JSONParser().parse(request)
        seller_serialize=SellerSerializer(data=mydict)
        if(seller_serialize.is_valid()):
            seller_serialize.save()
            return JsonResponse(seller_serialize.data)
        else:
            return HttpResponse("error in serialization")
    else:
        return HttpResponse("GET method")
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse
import json
from sellerapp.serializers import SellerSerializer
from sellerapp.models import Seller

@csrf_exempt
def seller_list(request):
    if(request.method=="GET"):
        sellers=Seller.objects.all()
        seller_serializer=SellerSerializer(sellers,many=True)
        return JsonResponse(seller_serializer.data,safe=False)
@csrf_exempt
def sellerPage(request):
    if(request.method=="POST"):
        getId=request.POST.get("sellerid")
        getName=request.POST.get("name")
        getAddress=request.POST.get("address")
        getPhono=request.POST.get("phono")
        mydict={"sellerid":getId,"name":getName,"address":getAddress,"phono":getPhono}
        seller_serialize=SellerSerializer(data=mydict)
        if(seller_serialize.is_valid()):
            seller_serialize.save()
            return JsonResponse(seller_serialize.data)
        else:
            return HttpResponse("error in serialization")
    else:
        return HttpResponse("no get method allowed")

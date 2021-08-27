from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from donors.serializers import DonorSerializer
from donors.models import Donor
from rest_framework.parsers import JSONParser
# Create your views here.
def registerDonor(request):
    return render(request,"register.html")

def searchDonor(request):
    return render(request,"search.html")


@csrf_exempt
def addDonor(request):
    if(request.method=="POST"):
        mydict=JSONParser().parse(request)
        donor_serialize=DonorSerializer(data=mydict)
        if(donor_serialize.is_valid()):
            donor_serialize.save()
            return JsonResponse(donor_serialize.data)
        else:
            return HttpResponse("error in serialization")
    else:
        return HttpResponse("GET method")


@csrf_exempt
def viewDonor(request):
    if(request.method=="GET"):
        donors=Donor.objects.all()
        donor_serialize=DonorSerializer(donors,many=True)
        return JsonResponse(donor_serialize.data,safe=False)

@csrf_exempt
def donorDetails(request,blood_group):
    try:
        donors=Donor.objects.get(blood_group=blood_group)
    except Donor.DoesNotExist:
        return HttpResponse("Invalid Blood Group")
    if(request.method=="GET"):
        donor_serialize=DonorSerializer(donors)
        return JsonResponse(donor_serialize.data,safe=False)
    if(request.method=="DELETE"):
        donors.delete()
        return HttpResponse("deleted")
    if(request.method=="PUT"):
        mydict=JSONParser().parse(request)
        donor_serialize=DonorSerializer(donors,data=mydict)
        if(donor_serialize.is_valid()):
            donor_serialize.save()
            return JsonResponse(donor_serialize.data)



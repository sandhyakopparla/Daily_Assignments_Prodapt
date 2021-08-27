from django.http import request
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'homeP.html')


def about(request):
    return render(request, 'aboutusP.html')
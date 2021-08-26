from django.urls import path,include
from rest_framework import parsers
from . import views
import villamanage

urlpatterns = [
    path('adddetail/',views.add,name='add'),
    
    path('first/',views.first,name='first'),
    path('regi/',views.reg,name='reg'),
    path('wel/',views.wel,name='wel'),
    path('norm/',views.normal,name='normal'),
    path('pre/',views.premium,name='premium'),
    
]
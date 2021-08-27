from django.urls import path, include
from businesspartner import views

urlpatterns =[ 
    path('h', views.home, name='home'),
    path('aboutus', views.about, name='about'),
]
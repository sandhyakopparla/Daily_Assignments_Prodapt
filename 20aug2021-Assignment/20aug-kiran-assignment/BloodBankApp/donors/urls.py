from django.urls import path,include
from .import views
urlpatterns = [
    path('add/', views.registerDonor,name='registerDonor'),
    path('adds/', views.searchDonor,name='searchDonor'),
    path('ad/', views.addDonor,name='addDonor'),
    path('viewall/', views.viewDonor,name='viewDonor'),
    path('view/<blood_group>', views.donorDetails,name='donorDetails'),
]
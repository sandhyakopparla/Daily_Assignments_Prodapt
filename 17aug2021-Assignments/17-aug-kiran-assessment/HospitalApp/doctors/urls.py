from django.urls import path,include
from . import views
urlpatterns = [
    path('add/',views.addDoctor,name='addDoctor'),
    path('viewall/',views.doctors_list,name='doctors_list'),
    path('viewdoctor/<fetchid>',views.doctors_details,name='doctors_details'),
]
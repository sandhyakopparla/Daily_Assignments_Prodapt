from django.urls import path,include
from . import views
urlpatterns =[
    path('add/',views.driverPage,name="driverPage"),
    path('viewall/',views.driver_list,name='driver_list'),
    path('viewdriver/<fetchid>',views.driver_details,name='driver_details'),
]
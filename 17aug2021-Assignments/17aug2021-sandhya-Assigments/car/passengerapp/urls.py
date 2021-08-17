from django.urls import path,include
from . import views
urlpatterns =[
    path('add/',views.passengerPage,name="passengerPage"),
    path('viewall/',views.passenger_list,name='passenger_list'),
    path('viewpassenger/<fetchid>',views.passenger_details,name='passenger_details'),
]
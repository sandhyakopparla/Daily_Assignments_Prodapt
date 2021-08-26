from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    ############   API   ############
    path('add/', views.flatadd,name='flatadd'),
    path('view/',views.flat_list,name='flat_list'),
    path('all/<id>',views.flatdetail,name='flatdetail'),
    path('search/',views.search,name='search'),
    path('update/',views.update,name='update'),
    path('delete/',views.delete,name='delete'),
    path('apiupdate/',views.apiupdate,name='apiupdate'),
    path('apidelete/',views.apidelete,name='apidelete'),

    #############   Webpage   #########

    path('addpage/',views.addpage,name='addpage'),
    path('',views.homepage,name='homepage'),
    path('searchpage/',views.searchpage,name='searchpage'),
    path('viewpage/',views.viewpage,name='viewpage'),
    path('updatepage/',views.updatepage,name='updatepage'),
    path('deletepage/',views.deletepage,name='deletepage'),


]
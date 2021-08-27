from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views
urlpatterns = [

    path('add/',views.add_flat,name="add_flats"),
    path('all/',views.view_flat,name="view_flats"),
    path('search/',views.search_flat,name="search_flats"),
    path('update/<bulding_no>',views.update,name="update_flats"),
    path('updateapi/',views.updateapi,name="update_flats"),
    path('updatedata/',views.update_flat,name="update_flats"),
    path('deleteapi/',views.deleteapi,name="delete_flats"),
    path('deletedata/',views.delete_data,name="delete_flats"),



    path('',views.home,name="view_flats"),
    path('add',views.add_page,name="add_flat_page"),
    path('view',views.view_page,name="view_flat_page"),
    path('search',views.search_page,name="search_page"),
    path('updateflat',views.update_page,name="search_page"),
    path('deleteflat',views.delete_page,name="delete_page"),




]
    
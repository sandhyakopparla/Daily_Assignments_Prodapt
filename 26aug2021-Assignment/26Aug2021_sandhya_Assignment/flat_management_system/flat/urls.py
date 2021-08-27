from django.urls import path,include
from . import views
urlpatterns =[
    #api
    path('add/',views.flatPage,name="flatPage"),
    path('viewall/',views.flat_list,name="flat_list"),
    path('viewflat/<fetchid>',views.flat_details,name='flat_details'),
    path('search/',views.searchapi,name='searchapi'),

    #html
    path('register/',views.flatregister_view,name="flatregister_view"),
    path('home/',views.home_view,name="home_view"),
    path('flatview/',views.viewall,name="viewall"),
    path('searchview/',views.search_view,name='search_view'),
    path('deletedata/',views.delete_data_read,name='delete_data_read'),
    path('deletescreen/',views.delete_view,name='delete_view'),
    path('updatescreen/',views.update_view,name='update_view'),
    path('delete_api/',views.delete_api,name='delete_api'),
    path('updatedata/',views.update_data_read,name='update_data_read'),
    path('updateapi/',views.update_api,name='update_api'),
    path('contact/',views.contact_view,name='contact_view'),
]
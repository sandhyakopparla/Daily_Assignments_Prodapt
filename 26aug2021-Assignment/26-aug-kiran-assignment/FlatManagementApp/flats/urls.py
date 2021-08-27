from django.urls import path,include
from . import views
urlpatterns = [
    path('add/', views.addFlat,name='addFlat'),
    path('viewall/', views.viewFlats,name='viewFlats'),
    path('view/<building_no>', views.FlatDetails,name='FlatDetails'),
    path('search/', views.searchapi,name='searchapi'),
    path('update/', views.update_api,name='update_api'),
    path('updatedata/', views.update_data_read,name='update_data_read'),
    path('delete/', views.delete_api,name='delete_api'),
    path('deletedata/', views.delete_data_read,name='delete_data_read'),


    path('page/', views.add_flat,name='add_flat'),
    path('viewflatpage/', views.viewingFlat,name='viewingFlat'),
    path('searchflatpage/', views.searchFlat,name='searchFlat'),
    path('updateflatpage/', views.updateFlat,name='updateFlat'),
    path('deleteflatpage/', views.deleteFlat,name='deleteFlat'),
]
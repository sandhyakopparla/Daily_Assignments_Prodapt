from django.urls import path,include
from . import views

urlpatterns = [
    #Views
    path('sub/',views.add_flat_view,name='add_flat_view'),
    # path('wel/',views.flat_view,name='flat_view'),
    path('viewallflat/',views.viewall_flat_view,name='viewall_flat_view'),
    path('searchview/',views.search_flat_view,name='search_flat_view'),
    path('viewupdate/',views.update_flat_view,name='update_flat_view'),
    path('viewdelete/',views.delete_flat_view,name='delete_flat_view'),


    #APIS
    path('add/',views.flat_create,name='flat_create'),
    path('viewall/',views.flat_list,name='flat_list'),
    path('view/<id>',views.flat_details,name='flat_details'),
    path('search/',views.searchapi,name='searchapi'),
    path('update_action_api/',views.update_data_read,name='update_data_read'),
    path('updatesearch/',views.updateapi,name='updateapi'),
    path('deletesearch/',views.deleteapi,name='deleteapi'),
    path('delete_action_api/',views.delete_data_read,name='delete_data_read'),
]
from django.urls import path,include
from . import views
urlpatterns = [
    path('add/',views.add_details,name='add_details'),
    path('viewall/',views.view_details,name='view_details'),
    path('view/<fetchid>',views.view_single,name='view_single'),
    path('search/',views.search,name='search'),
    path('update/',views.update,name='update'),
    path('updateact/',views.action_update,name='action_update'),
    path('delete/',views.delete,name='delete'),
    path('deleteact/',views.action_delete,name='action_delete'),

    path('homeui/',views.home,name='home'),
    path('addui/',views.add,name='add'),
    path('showui/',views.show,name='show'),
    path('searchui/',views.searchone,name='searchone'),
    path('updateui/',views.updateone,name='updateone'),
    path('deleteui/',views.deleteone,name='deleteone'),
    
    
    
    
    
    
]
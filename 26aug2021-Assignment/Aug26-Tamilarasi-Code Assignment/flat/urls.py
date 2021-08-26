from django.urls import path, include
from . import views

urlpatterns = [
    path('flat/',views.myFlat,name='myFlat'),
    path('delete/',views.myDelete,name='myDelete'),
    path('update/',views.myUpdate,name='myUpdate'),
    path('welcome/',views.myWelcomePage,name='myWelcomePage'),
    path('viewallflat/',views.myViewAllPage,name='myViewAllPage'),
    path('searchflat/',views.mySearch,name='mySearch'),

    path('deletesearch/',views.DeleteSearchAPI,name='DeleteSearchAPI'),
    path('deleteread/',views.DeleteRead,name='DeleteRead'),
    path('updateread/',views.UpdateRead,name='UpdateRead'),
    path('updatesearch/',views.UpdateSearchAPI,name='UpdateSearchAPI'),
    path('search/',views.SearchAPI,name='SearchAPI'),
    path('add/',views.myFlatPage,name='myFlatPage'),
    path('viewall/',views.myFlatList,name='myFlatList'),
    path('viewflat/<id>',views.myFlatDetails,name='myFlatDetails'),
]
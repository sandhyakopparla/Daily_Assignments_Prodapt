from django.urls import path,include
from.import views
urlpatterns=[

    path("addf/",views.addflat,name="addflat"),
    path("viewflats/",views.veiwallflats,name="viewallflats"),
    path("update/",views.updateflats,name="updateflats"),
    path("delete/",views.deleteflats,name="deleteflats"),
    path('searchflat/',views.searchflat,name='searchflat'),



    path('add/',views.flat,name='flat'),
    path('viewall/',views.flat_list,name='flat_list'),
    path('search/',views.searchapi,name='searchapi'),
    path('updatesearch/',views.updateapi,name='updateapi'),
    path('updateApi/',views.update_data,name='update_data'),
    path('deletesearch/',views.deleteapi,name='deleteapi'),
    path('deleteApi/',views.delete_data,name='delete_data'),

    path('view/<fetchid>',views.myflats,name='myflats'),
]
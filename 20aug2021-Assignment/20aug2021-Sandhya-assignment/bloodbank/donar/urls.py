from django.urls import path,include
from . import views
urlpatterns =[
    path('register/',views.blood_view,name="blood_view"),
    path('search/',views.search_view,name="search_view"),
    path('add/',views.donarPage,name="donarPage"),
    path('viewall/',views.donar_list,name="donar_list"),
    path('viewit/<fetchblood_group>',views.donar_details,name="donar_details"),
]
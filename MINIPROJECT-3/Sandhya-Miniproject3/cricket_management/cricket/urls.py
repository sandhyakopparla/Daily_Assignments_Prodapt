from django.urls import path,include
from . import views
urlpatterns =[
    #api
    path('add/',views.cricketPage,name="cricketPage"),
    path('viewall/',views.cricket_list,name="cricket_list"),
    path('viewit/<fetchid>',views.cricket_details,name="cricket_details"),

    #html
    path('register/',views.register_view,name="register_view"),
    path('view/',views.view_all,name="view_all"),
    path('update/',views.update_all,name="update_all"),
    path('delete/',views.delete_all,name="delete_all"),

]
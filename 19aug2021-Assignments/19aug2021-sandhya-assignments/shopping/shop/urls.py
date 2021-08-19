from django.urls import path,include
from . import views
urlpatterns =[
    path('register/',views.shop_view,name="shop_view"),
    path('add/',views.shopPage,name="shopPage"),
    path('viewall/',views.shop_list,name="shop_list"),
    path('viewit/<fetchid>',views.shop_details,name="shop_details"),
]


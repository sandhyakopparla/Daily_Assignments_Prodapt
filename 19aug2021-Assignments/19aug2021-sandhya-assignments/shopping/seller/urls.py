from django.urls import path,include
from . import views
urlpatterns =[
    path('add1/',views.seller_view,name="seller_view"),
    path('add/',views.sellerPage,name="sellerPage"),
    path('viewall/',views.seller_list,name="seller_list"),
    path('viewit/<fetchid>',views.seller_details,name="seller_details"),
]


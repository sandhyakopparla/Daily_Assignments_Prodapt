from django.urls import path,include
from . import views
urlpatterns =[
    path('add1/',views.product_view,name="product_view"),
    path('add/',views.productPage,name="productPage"),
    path('viewall/',views.product_list,name='product_list'),
    path('viewit/<fetchid>',views.product_details,name="product_details"),
   

]
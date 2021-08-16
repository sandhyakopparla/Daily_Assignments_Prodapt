from django.urls import path,include
from . import views
urlpatterns = [
    path('add/',views.productPage,name="productPage"),
    path('viewall/',views.product_list,name='product_list'),
]
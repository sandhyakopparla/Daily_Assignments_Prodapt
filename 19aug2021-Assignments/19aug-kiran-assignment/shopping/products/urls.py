from django.urls import path,include
from . import views
urlpatterns = [
    path('add/', views.add_product,name='add_product'),
    path('a/', views.addproduct,name='addproduct'),
    path('viewall/', views.viewproduct,name='viewproduct'),
    path('view/<fetchid>', views.productDetails,name='productDetails'),
]
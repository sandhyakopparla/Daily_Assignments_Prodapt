from django.urls import path,include
from . import views
urlpatterns = [
    path('add/', views.add_seller,name='add_seller'),
    path('a/', views.addseller,name='addseller'),
    path('viewall/', views.viewseller,name='viewseller'),
    path('view/<fetchid>', views.sellerDetails,name='sellerDetails'),
]
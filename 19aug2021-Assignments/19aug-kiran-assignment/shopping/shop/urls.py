from django.urls import path,include
from . import views
urlpatterns = [
    path('register/', views.add_page,name='add_page'),
    path('add/', views.addShop,name='addShop'),
    path('addall/', views.viewShop,name='viewShop'),
    path('view/<fetchid>', views.shopDetails,name='shopDetails'),
]

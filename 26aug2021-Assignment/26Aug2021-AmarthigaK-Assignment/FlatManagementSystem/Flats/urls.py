from django.urls import path, include
from Flats import views 

urlpatterns = [
    #
    path('add/', views.add, name="add"),
    path('viewall/', views.viewall, name="viewall"),
    path('view/<id>', views.updel, name="updel"),
    path('search/', views.search, name="search"),

    path('', views.home, name="home"),
    path('search/', views.search, name='search'),
    path('signup/', views.signup, name='signup'),
    path('user/', views.user, name='user'),
    path('login/', views.login, name='login'),
    path('aboutus/', views.aboutus, name='aboutus'),

]
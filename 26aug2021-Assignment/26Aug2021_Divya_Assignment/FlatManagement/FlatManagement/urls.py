from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('flat/',include('Flats.urls')),
    path('villa/',include('villamanage.urls')),
]

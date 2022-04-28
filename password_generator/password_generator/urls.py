from django.contrib import admin
from django.urls import path, include
from generator import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('generator/', include('generator.urls')),
    path('', include('generator.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('', include('django.contrib.auth.urls')),
    path('users/', include('users.urls')),
    path('', include('users.urls')),
]

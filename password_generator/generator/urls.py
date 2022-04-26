from django.urls import path
from generator import views

urlpatterns = [
    path('about', views.about, name='about'),
    path('', views.index, name='index'),
    path('generate-password', views.password, name='password'),
]

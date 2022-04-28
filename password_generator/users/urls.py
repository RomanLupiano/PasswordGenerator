from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login_user/', views.login_user, name='login'),
    path('logout/', LogoutView.as_view(template_name='authenticate/logout.html'), name='logout'),
    path('user_home/', views.user_home, name='home'),
    path('user_home/passwordcreate', views.CreatePassword, name='create'),
]

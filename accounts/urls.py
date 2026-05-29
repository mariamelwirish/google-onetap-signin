from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_page, name='login'),
    path('auth/', views.auth_receiver, name='auth_receiver'),
    path('home/', views.home, name='home'),
]
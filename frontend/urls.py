from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name="home"),
    path('register/', views.register_request, name="register"),
    path('rodo/', views.rodo, name="rodo"),
    path('polityka_prywatnosci/', views.polityka_prywatnosci, name="polityka_prywatnosci"),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name="home"),
    path('register/', views.register_request, name="register"),
]
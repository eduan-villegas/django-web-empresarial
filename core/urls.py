from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home,name='home'),
    path('about/', views.About,name='about'),
    path('store/', views.Store,name='store'),
    path('contact/', views.Contact,name='contact'),
]
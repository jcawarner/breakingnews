from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('social/', views.social, name='social'),
    path('', views.general, name='general'),
    path('science/', views.science, name='science'),
    path('technology/', views.technology, name='technology'),
    path('business/', views.business, name='business'),
    path('health/', views.health, name='health'),
    path('entertainment/', views.entertainment, name='entertainment'),
    path('search/', views.search, name='search'),
]

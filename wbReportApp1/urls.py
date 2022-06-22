from django.contrib import admin
from django.urls import path
from .views import index, parseWB


urlpatterns = [
    path('', index, name = "indexPage"),
    path('parseWB', parseWB, name = "parseWB"),
 
]

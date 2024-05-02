from django.contrib import admin
from django.urls import path
from GivingWay import views






urlpatterns = [
    path("",views.index),
]

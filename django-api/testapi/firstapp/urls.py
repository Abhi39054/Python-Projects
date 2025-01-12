
from django.contrib import admin
from django.urls import path, include
from .views import TestApi

urlpatterns = [
    path('', TestApi.as_view(), name="TestApi")
]

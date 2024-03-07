from django.contrib import admin
from django.urls import path

from new import views

urlpatterns = [
    path("", views.index,name='new'),
]

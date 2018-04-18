from django.urls import path
from django.views.generic import ListView, DetailView
from . import views

urlpatterns = [
	path('', views.index)
]
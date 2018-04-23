from django.urls import path
from django.views.generic import ListView, DetailView
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
	# path('', views.index)
	path('stocks', views.StockList.as_view())

]
urlpatterns = format_suffix_patterns(urlpatterns)
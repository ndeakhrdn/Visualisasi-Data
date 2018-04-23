from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Fakulti, Comment
from django.db.models import Q
from .forms import UploadFileForm
from tablib import Dataset
from django.views.generic.edit import FormView
from rest_framework import serializers

import numpy as np
# Create your views here.

class CommentSerializer(serializers.Serializer):
	email = serializers.EmailField()
	content = serializers.CharField(max_length=200)
	created = serializers.DateTimeField()

	def create(self, validated_data):
		return Comment(**validated_data)

	def update(self, instance, validated_data):
		instance.email = validated_data.get('email', instance.email)
		instance.content = validated_data.get('content', instance.content)
		instance.created = validated_data.get('created', instance.created)
		return instance


def index(request):
	fakulti = Fakulti.objects.exclude(
	  Q(fakulti__isnull=True)|Q(fakulti='')).values_list('fakulti', flat=True).distinct().order_by('fakulti')
	return render(request, "home/index.html", {'fakulti' : fakulti})

def admins(request):  
	
	return render(request, "admin/index.html")

def simple_upload(request):
	if request.method == 'POST':
		person_resource = PersonResource()
		dataset = Dataset()
		new_persons = request.FILES['myfile']

		imported_data = dataset.load(new_persons.read())
		result = person_resource.import_data(dataset, dry_run=True)  # Test the data import

		if not result.has_errors():
			person_resource.import_data(dataset, dry_run=False)  # Actually import now

	return render(request, 'core/simple_upload.html')


#------------------------------------------------------------------------------------
from django.views.generic import View

class HomeView(View):
	def get(self, request, *args, **kwargs):
		return render(request, 'home/chart.html', {})

def get_data(request, *args, **kwargs):
	data = {
		"sale":100,
		"customers":10,
	}
	return JsonResponse(data) #HttpResponse

# ------------------ serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import FakultiSerializer

# Lists all fakulti or create a new one
class FakultiList(APIView):
	def get(self):
		fakulti = Fakulti.objects.all()
		serializer = FakultiSerializer(fakulti, many=True)
		return Response(fakulti.data)
		pass

	def post(self):
		pass


from django.shortcuts import render
from .models import Fakulti
from django.db.models import Q

from tablib import Dataset
# Create your views here.

def index(request):
	fakulti = Fakulti.objects.exclude(
      Q(fakulti__isnull=True)|Q(fakulti='')).values_list('fakulti', flat=True).distinct().order_by('fakulti')
	return render(request, "home/index.html", {'fakulti' : fakulti})

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
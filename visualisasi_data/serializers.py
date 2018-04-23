from rest_framework import serializers
from .models import Fakulti

class FakultiSerializer(serializers.ModelSerializer):
	class Meta:
		model = Fakulti
		# fields = ("nama", "ukm_per")
		fields = '__all__'
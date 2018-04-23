from django.db import models

# Create your models here.

# ---------------SERIALIZER-----------------
from datetime import datetime

class Comment(object):
    def __init__(self, email, content, created=None):
        self.email = email
        self.content = content
        self.created = created or datetime.now()

comment = Comment(email='leila@example.com', content='foo bar')

#---------------------------------------------

class Person(models.Model):
	name = models.CharField(max_length=30)
	email = models.EmailField(blank=True)
	birth_date = models.DateField()
	location = models.CharField(max_length=100, blank=True)

class Fakulti(models.Model):
	ukm_per = models.CharField(max_length=7)
	nama = models.CharField(max_length=100)
	status_semasa = models.CharField(max_length=100)
	status_cuti = models.CharField(max_length=100, blank=True)
	jabatan = models.CharField(max_length=255)
	fakulti = models.CharField(max_length=255)
	jawatan = models.CharField(max_length=255)
	lantikan = models.CharField(max_length=255, blank=True, null= True)
	tarikh_lantikan = models.CharField(max_length=255, blank=True, null= True)
	tarikh_tamat_jawatan = models.CharField(max_length=255, blank=True, null= True)
	tarikh_mula_cuti = models.CharField(max_length=255, blank=True, null= True)
	tarikh_tamat_cuti = models.CharField(max_length=255, blank=True, null= True)
	jam_latihan = models.CharField(max_length=255, blank=True, null= True)

	

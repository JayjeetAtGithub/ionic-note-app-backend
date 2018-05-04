from django.db import models
from datetime import datetime
# Create your models here.

class Note(models.Model):
	body = models.CharField(max_length=1000)
	date_created = models.DateTimeField(default=datetime.now)
	uid = models.CharField(max_length=255,default='')

	def __str__(self):
		return self.body


class User(models.Model):
	uid = models.CharField(max_length=255,default='')
	email = models.CharField(max_length=255,default='')
	displayName = models.CharField(max_length=255,default='')
	photoURL = models.CharField(max_length=255,default='')


	def __str__(self):
		return self.displayName

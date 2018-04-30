from django.db import models
from datetime import datetime
# Create your models here.



class Note(models.Model):
	body = models.CharField(max_length=1000)
	date_created = models.DateTimeField(default=datetime.now)
	user_id = models.IntegerField(default=0)

	def __str__(self):
		return self.body


class User(models.Model):
	email = models.CharField(max_length=255)
	displayName = models.CharField(max_length=255)
	photoURL = models.CharField(max_length=255)


	def __str__(self):
		return self.displayName 


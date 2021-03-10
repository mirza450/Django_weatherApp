from django.db import models

# Create your models here.

class weather(models.Model):
	city= models.CharField(max_length=100)
	desc=models.CharField(max_length=50)
	temp=models.CharField(max_length=20)
	humidity=models.CharField(max_length=20)

	def __str__(self):
		return self.city
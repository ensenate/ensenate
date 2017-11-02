from django.db import models

# Create your models here.

class Unidad(models.Model):
	titulo = models.CharField(max_length=30, blank=False)
	
	def __str__(self):
		return self.titulo
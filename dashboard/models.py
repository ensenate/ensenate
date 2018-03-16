from django.db import models
from django.contrib.auth.models import  AbstractUser

# Create your models here.

class Unidad(models.Model):
	titulo = models.CharField(max_length=30, blank=False)
	image = models.ImageField(upload_to='curso/unidades/')

	def __str__(self):
		return self.titulo

class Leccion(models.Model):
	titulo = models.CharField(max_length=30, blank=False)
	bloqueado = models.BooleanField(default=True)
	
	unidad = models.ForeignKey(Unidad)

	def __str__(self):
		return self.titulo

class Palabra(models.Model):
	titulo = models.CharField(max_length=30, blank=False)
	image = models.ImageField(upload_to='curso/palabras/')
	image2 = models.ImageField(default='curso/palabras/no-imagen.jpg', null=True, blank=True, upload_to='curso/palabras/')
	
	leccion = models.ForeignKey(Leccion)
	
	def __str__(self):
		return self.titulo

from django.db import models
from django.utils import timezone

# Create your models here.

class Contacto(models.Model):
	asunto = models.CharField(max_length=30, blank=False)
	email = models.EmailField(max_length=254, unique=False)
	mensaje = models.TextField(max_length=350)
	fecha  = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.email
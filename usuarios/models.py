from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.

class User(AbstractUser):
	biografia = models.CharField(max_length=255, blank=True, default='',null=False)
	nivel = models.PositiveIntegerField(default=0)
	gemas = models.PositiveIntegerField(default=0)
	fecha_inicio = models.DateField(default=timezone.now)
	image = models.ImageField(upload_to='usuarios/perfiles/', default='usuarios/default/perfil.png')


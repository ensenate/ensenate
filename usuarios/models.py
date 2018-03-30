from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

from dashboard.models import Unidad


# Create your models here.

class User(AbstractUser):
	biografia = models.CharField(max_length=255, blank=True, default='',null=False)
	nivel = models.PositiveIntegerField(default=0)
	gemas = models.PositiveIntegerField(default=0)
	fecha_inicio = models.DateField(default=timezone.now)
	image = models.ImageField(upload_to='usuarios/perfiles/', default='usuarios/default/perfil.png')

	cargar_datos = models.BooleanField(default=False)

class DatosUnidadUsuario(models.Model):
	usuario = models.ForeignKey(User, on_delete = models.CASCADE)
	unidad = models.ForeignKey(Unidad, on_delete = models.CASCADE)

	ultima_vez = models.DateField(null=True)
	fuerza = models.PositiveSmallIntegerField(default=0)
	bloqueado = models.BooleanField(default=True)
	completo = models.BooleanField(default=False)

	def __str__(self):
		return self.usuario.first_name + " - " + self.unidad.titulo

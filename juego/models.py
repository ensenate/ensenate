from django.db import models
from usuarios.models import User
# Create your models here.

class Puntuacion(models.Model):
	usuario = models.ForeignKey(User)
	juego = models.CharField(max_length=50, null=True)
	puntos = models.PositiveIntegerField(default=0)

	def __str__(self):
		return self.usuario.username + ' - ' + self.juego


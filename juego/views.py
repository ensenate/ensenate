from django.shortcuts import render, redirect

#decoradores
from django.contrib.auth.decorators import login_required

#models
from .models import Puntuacion

# Create your views here.

def puntuacion(usuario, juego):
	puntuacion = Puntuacion.objects.filter(usuario=usuario, juego=juego)

	if not puntuacion:
		puntuacion = Puntuacion(usuario=usuario, juego=juego, puntos=0)
		puntuacion.save()

	puntuacion = Puntuacion.objects.filter(usuario=usuario, juego=juego)
	
	for p in puntuacion:
		puntos = p.puntos

	return puntos

def mejores_puntuaciones(juego):
	mejores = Puntuacion.objects.filter(juego=juego).order_by('puntos').reverse()[:3]
	return mejores


@login_required
def juego (request, nombre_juego):
	usuario = request.user
	context = {}
	
	if nombre_juego == 'snake' or nombre_juego == 'flappybird':
		if usuario.gemas > 0:
			usuario.gemas = usuario.gemas - 1
			usuario.save()

			puntos = puntuacion(usuario, nombre_juego)
			

			best_score = mejores_puntuaciones(nombre_juego)

			print (puntos)

			context = {
				'puntos':puntos,
				'mejorespuntuaciones':best_score,
				'juego':nombre_juego,
			}

		else:
			return redirect('perfil')
	else:
		return redirect('perfil')

	template = 'juego/'  + nombre_juego + '.html'
	return render(request, template, context)

@login_required
def guardar (request, nombre_juego, puntos):
	usuario = request.user
	puntos_viejos = puntuacion(usuario, nombre_juego)
	
	puntos = int(puntos)
	puntos_viejos = int(puntos_viejos)
	
	if puntos > puntos_viejos:
		puntos_nuevos = Puntuacion.objects.get(usuario=usuario, juego=nombre_juego)
		puntos_nuevos.puntos = puntos
		puntos_nuevos.save()

	return redirect('perfil')
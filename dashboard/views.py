from django.shortcuts import render, get_object_or_404

#decoradores
from django.contrib.auth.decorators import login_required

#vistas basadas en clases
from django.views.generic import TemplateView


#prueba
from .models import Unidad, Leccion, Palabra#Category, Item#

#prueba 2 
from usuarios.models import DatosUnidadUsuario, DatosLeccionUsuario

def  verificar_unidades(usuario):
	if not DatosUnidadUsuario.objects.filter(usuario=usuario):
		unidades = Unidad.objects.all()

		x=0
		
		for unidad in unidades:
			x = x + 1
			if x <= 3:
				bloqueado = False
			else:
				bloqueado = True
			
			unidad_usuario = DatosUnidadUsuario(usuario=usuario, unidad=unidad, bloqueado=bloqueado)
			unidad_usuario.save()
		else:
			return

#esta funcion no esta al 100% ojo hay que agregar p'rimero todas las lecciones a la base de datos y luego asi agregar a la base de datos todo
def verificar_lecciones(usuario):
	
	x=0

	if not DatosLeccionUsuario.objects.filter(usuario=usuario):
		unidades = Unidad.objects.all()

		x = x + 1
		if x <= 3:
			bloqueado = False
		else:
			bloqueado = True

		for unidad in unidades:

			for leccion in unidad.leccion_set.filter(unidad=unidad):
				leccion_usuario = DatosLeccionUsuario(usuario=usuario, unidad=unidad, leccion=leccion, bloqueado=bloqueado)
				leccion_usuario.save()
	else:
		return



@login_required
def inicio(request):
	template = 'dashboard/dashboard.html'
	
	verificar_unidades(request.user)
	verificar_lecciones(request.user)

	unidades = Unidad.objects.all()

	context = {
		'unidades':unidades,
	}


	return render(request,template,context)

@login_required
def perfil(request):
	template = 'dashboard/perfil.html'
	return render(request, template, {})

@login_required
def detalle_unidad(request, unidad):
	template = 'dashboard/lecciones.html'
	get_object_or_404(Unidad, titulo=unidad)

	unidades = Unidad.objects.get(titulo=unidad)
	lecciones = unidades.leccion_set.filter(unidad=unidades)
	palabras = Palabra.objects.filter(leccion=lecciones[0])
	
	return render(request, template, {'unidades':unidades, 'lecciones':lecciones, 'palabras':palabras})

@login_required
def practica(request, unidad, leccion):
	template = 'dashboard/practica.html'
	get_object_or_404(Unidad, titulo=unidad)

	unidades = Unidad.objects.get(titulo=unidad)
	
	lecciones = Leccion.objects.get(pk=leccion)

	palabras = lecciones.palabra_set.all()
	

	return render(request, template, {'lecciones':lecciones, 'unidades':unidades, 'palabras':palabras})

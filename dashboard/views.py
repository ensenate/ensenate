from django.shortcuts import render, get_object_or_404, redirect

#decoradores
from django.contrib.auth.decorators import login_required

#vistas basadas en clases
from django.views.generic import TemplateView


#prueba
from .models import Unidad, Leccion, Palabra#Category, Item#

#prueba 2 
from usuarios.models import DatosUnidadUsuario, DatosLeccionUsuario

#ramdon
from random import randint

# json
import json


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

def verificar_lecciones(usuario):
	if not DatosLeccionUsuario.objects.filter(usuario=usuario):
		unidades = Unidad.objects.all()
		x=0

		for unidad in unidades:

			x = x + 1
			if x <= 3:
				bloqueado = False
			else:
				bloqueado = True

			for leccion in unidad.leccion_set.filter(unidad=unidad):
				leccion_usuario = DatosLeccionUsuario(usuario=usuario, unidad=unidad, leccion=leccion, bloqueado=bloqueado)
				leccion_usuario.save()
	else:
		return

@login_required
def inicio(request):
	template = 'dashboard/dashboard.html'
	
	if not request.user.cargar_datos:
		verificar_unidades(request.user)
		verificar_lecciones(request.user)
		request.user.cargar_datos = True
		request.user.save()

	unidades = Unidad.objects.all()

	unidad_usuario = DatosUnidadUsuario.objects.filter(usuario=request.user)

	datos = zip(unidades,unidad_usuario)

	context = {
		'datos':datos,
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
def vista_previa(request, unidad, leccion):
	template = 'dashboard/vista_previa.html'
	get_object_or_404(Unidad, titulo=unidad)

	unidades = Unidad.objects.get(titulo=unidad)
	
	lecciones = Leccion.objects.get(pk=leccion)

	palabras = lecciones.palabra_set.all()
	

	return render(request, template, {'unidad':unidades, 'palabras':palabras, 'leccion':leccion})

@login_required
def aprender(request, unidad, leccion):
	template = 'dashboard/aprender.html'

	unidades = Unidad.objects.get(titulo=unidad)
	lecciones = Leccion.objects.get(pk=leccion)
	palabras = lecciones.palabra_set.all()

	dic = {}
	dic_p = {}
	list_dic = []
	cont = 0

	for p in palabras:
		cont += 1
		dic_p["titulo"] = p.titulo
		dic_p["image"] = p.image.url
		dic_p["image2"] = p.image2.url
		
		list_dic.append(dic_p)


		del dic_p

		dic_p = {}

	dic["imagenes"] = list_dic


	data = json.dumps(dic)

	print data

	context = {
		'datos':data,
		'unidades':unidades,
		'leccion':leccion,
	}
	
	return render(request, template, context)


@login_required
def confirmar(request, unidad, leccion):
	return redirect('../../perfil/');
from django.shortcuts import render, get_object_or_404, redirect

#decoradores
from django.contrib.auth.decorators import login_required

#vistas basadas en clases
from django.views.generic import TemplateView


#prueba
from .models import Unidad, Leccion, Palabra#Category, Item#

#prueba 2 
from usuarios.models import DatosUnidadUsuario

#ramdon
from random import randint

# json
import json

#timezone
from django.utils import timezone



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

@login_required
def inicio(request):
	template = 'dashboard/dashboard.html'
	
	if not request.user.cargar_datos:
		verificar_unidades(request.user)
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
	bloqueado = True

	if request.user.gemas > 0:
		bloqueado = False

	return render(request, template, {'bloqueado':bloqueado,})

@login_required
def detalle_unidad(request, unidad):
	template = 'dashboard/lecciones.html'
	get_object_or_404(Unidad, titulo=unidad)


	unidades = Unidad.objects.get(titulo=unidad)
	lecciones = unidades.leccion_set.filter(unidad=unidades)
	palabras = Palabra.objects.filter(leccion=lecciones[0])

	fecha = DatosUnidadUsuario.objects.filter(usuario=request.user, unidad=unidades)
	fecha = fecha[0].ultima_vez

	if fecha:
		cadena = fecha.strftime("%d-%m-%y")
	else:
		cadena = None

	return render(request, template, {'unidades':unidades, 'lecciones':lecciones, 'palabras':palabras, 'fecha':cadena,})

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

	context = {
		'datos':data,
		'unidades':unidades,
		'leccion':leccion,
	}
	
	return render(request, template, context)


@login_required
def confirmar(request, unidad):

	unidad = get_object_or_404(Unidad, titulo=unidad)

	datos = DatosUnidadUsuario.objects.filter(usuario=request.user)

	print datos

	for i in xrange(0, len(datos)):
		
 		if datos[i].unidad == unidad:
 			datos[i].completo = True
 			datos[i].ultima_vez = timezone.now()
			datos[i].save()

			user = request.user
			user.gemas += 1
			user.save()

			siguiente = i + 1
			if siguiente <= len(datos) - 2:
				datos[siguiente].bloqueado = False
				datos[siguiente].save()
		
	return redirect('../../dashboard/')
from django.shortcuts import render, get_object_or_404

#decoradores
from django.contrib.auth.decorators import login_required

#vistas basadas en clases
from django.views.generic import TemplateView


#prueba
from .models import Unidad, Leccion, Palabra#Category, Item#


@login_required
def inicio(request):
	template = 'dashboard/dashboard.html'

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

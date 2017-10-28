from django.shortcuts import render, redirect

#decoradores
from django.contrib.auth.decorators import login_required

#modelos
from django.contrib.auth.models import User

#authenticacion
from django.contrib.auth import authenticate 
from django.contrib.auth import login

#vistas-clases
from django.views.generic import TemplateView, CreateView

#formularios
from .forms import crear_usuario_form


# Create your views here.

class inicio (TemplateView):
	template_name = 'principal/inicio.html'

def registrar_usuario(request):
	template = "principal/registro.html"
	
	if request.method == 'POST':
        		form = crear_usuario_form(request.POST)
        		if form.is_valid():
            			form.save()
            			usuario = form.cleaned_data.get('username')
            			password = form.cleaned_data.get('password1')
            			
            			user = authenticate(username=usuario, password=password)
            			
            			login(request, user)
            			return redirect('dashboard')
	else:
		form = crear_usuario_form()
	
	context = {
		'form':form,
	}
	return render(request, template, context)



@login_required
def dashboard(request):
	template = 'principal/dashboard.html'
	context = {

	}
	return render(request, template, context)


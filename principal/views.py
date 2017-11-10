from django.shortcuts import render, redirect

#decoradores
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect

#modelos
from usuarios.models import User
from .models import Contacto


#authenticacion
from django.contrib.auth import authenticate 
from django.contrib.auth import login

#vistas-clases
from django.views.generic import TemplateView, CreateView
from django.template.response import TemplateResponse

#formularios
from .forms import crear_usuario_form, restablecer_password_form, contacto_form

#tokens
from django.contrib.auth.tokens import default_token_generator

#urls
from django.core.urlresolvers import reverse


# Create your views here.

def inicio (request):
	template = 'principal/inicio.html'
	if request.user.is_authenticated():
		return redirect('dashboard')
	return render(request,template,{})
	

@csrf_protect
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

@csrf_protect
def restablecer_password(request, subject_template_name='registration/password_reset_subject.txt', 	token_generator=default_token_generator, post_reset_redirect=None, from_email=None, html_email_template_name=None):

		post_reset_redirect = reverse('password_reset_done')
		template = 'principal/restaurar-password/password_reset_form.html'
		email_template_name = 'principal/restaurar-password/password_reset_email.html'

		if request.method == "POST":
			form = restablecer_password_form(request.POST)

			if form.is_valid():
				opts = {
					'use_https': request.is_secure(),
					'token_generator': token_generator,
					'from_email': from_email,
					'email_template_name': email_template_name,
					'subject_template_name': subject_template_name,
					'request': request,
					'html_email_template_name': html_email_template_name,
					}
				user = User.objects.filter(email=form.cleaned_data.get('email'))
				if  user:
					form.save(**opts)
					return redirect(post_reset_redirect)
				else:
					error = "no hay un usuario asociado a este correo"
					print("no hay usuario")
					context = {
						'form': form,
						'error':error,
					}
		else:
			form = restablecer_password_form()
			context = {
				'form': form,
			}
		return TemplateResponse(request, template, context)


class contactanos(CreateView):
	model = Contacto
	form_class = contacto_form
	template_name = 'principal/contactanos.html'
	success_url = '/envio_correcto/' 

class envio_correcto (TemplateView):
	template_name = 'principal/envio_correcto.html'
from django.shortcuts import render, get_object_or_404, render_to_response, RequestContext

from .forms import actualizar_cuenta, actualizar_perfil, actualizar_pass

from django.contrib.auth.forms import PasswordChangeForm

from django.contrib.auth import update_session_auth_hash

# Create your views here.

#Importamos el modelo User
from .models import User

#decoradores
from django.contrib.auth.decorators import login_required

@login_required
def conf_cuenta(request):


	template = 'dashboard/conf_cuenta.html'
	mensaje = ''
	user = get_object_or_404(User,pk= request.user.pk)
	
	if request.method == "POST":
		form = actualizar_cuenta(request.POST, request.FILES, instance=user)
		
		if form.is_valid():
			form.save()
			mensaje = 'datos actualizados con exito'

			return render_to_response(template, locals(), context_instance=RequestContext(request))

	else:
		form = actualizar_cuenta(instance=user)
		mensaje = ''

	return render(request, template, {'form':form})

@login_required
def conf_perfil(request):
	template = 'dashboard/conf_perfil.html'
	mensaje = ''
	user = get_object_or_404(User,pk=request.user.pk)
	
	if request.method == "POST":
		form = actualizar_perfil(request.POST, instance=user)
		
		if form.is_valid():
			form.save()
			mensaje = 'datos actualizados con exito'

			return render_to_response(template, locals(), context_instance=RequestContext(request))
	else:
		form = actualizar_perfil(instance=user)
		mensaje = ''

	return render(request, template, {'form':form, 'mensaje':mensaje})

@login_required
def conf_pass(request):
	template = 'dashboard/conf_pass.html'
	mensaje = ''
	user = get_object_or_404(User,pk=request.user.pk)
	
	if request.method == "POST":
		form = PasswordChangeForm(request.user, request.POST)
		
		if form.is_valid():

			usuario = form.save()
			update_session_auth_hash(request, usuario)  # Important!
	#		form.save()
			mensaje = 'datos actualizados con exito'
#
#			return render_to_response(template, locals(), context_instance=RequestContext(request))
	else:
		form = PasswordChangeForm(request.user)
#		mensaje = ''

	return render(request, template, {'form':form, 'mensaje':mensaje})

@login_required
def ayuda(request):
	template = 'usuario/ayuda.html'
	return render(request, template,{})	

from django.shortcuts import render

#decoradores
from django.contrib.auth.decorators import login_required

#vistas basadas en clases
from django.views.generic import TemplateView


@login_required
def inicio(request):
	template = 'dashboard/dashboard.html'
	context = {

	}
	return render(request,template,context)


from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def dashboard(request):
	template = 'principal/dashboard.html'
	context = {

	}
	return render(request, template, context)

def  inicio(request):
	template = 'principal/inicio.html'
	context = {

	}
	return render(request, template, context)

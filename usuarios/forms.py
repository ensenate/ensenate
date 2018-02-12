# -*- coding: utf-8 -*-
from django import forms
from .models import User

class actualizar_cuenta(forms.ModelForm):
	
	username = forms.RegexField(
		label = "Usuario", 
		max_length = 20,
		regex = r"^[\w.@+-]+$",
		error_messages = { 'invalid':'puede contener solo letras, números y caracteres @ /. / + / - / _.',
					'unique': 'ya existe este usuario.',  'required': 'este campo es obligatorio' },
		widget = forms.TextInput( attrs = { 'class': 'form-control','placeholder':'ingresa tu usuario' } ),#se le puede poner todos los atributos del html
		)

	email = forms.CharField(
	label = "Correo Electronico",
	error_messages = { 'invalid':'ingresa un correo electronico valido', 'required': 'este campo es obligatorio' },
	widget = forms.TextInput( attrs = { 'class': 'form-control', 'type': 'email', 'placeholder':'ingresa tu correo electronico' } ),
	)

	image = forms.ImageField(
		)


	class Meta:
		model = User
		fields = ('username','email','image')


class actualizar_perfil(forms.ModelForm):
	
	first_name = forms.CharField(
		label = "Nombre",
		error_messages = { 'required': 'este campo es obligatorio' },
		widget = forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder':'ingresa tu nombre'} ),
		)


	last_name = forms.CharField(
		label = "Apellido",
		error_messages = { 'required': 'este campo es obligatorio' },
		widget = forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder':'ingresa tu apellido'} ),
		)

	biografia = forms.CharField(
		required = False, 
		label = "Biografia",
		widget = forms.Textarea(attrs={'class': 'form-control', 'type': 'text', 'placeholder':'ingresa una biografia', 'cols':'26', 'rows':'4',}),
	)



	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'biografia')

class actualizar_pass(forms.ModelForm):

	password1 = forms.CharField(
		label = "Actual Contraseña",
		required = True,
		error_messages = { 'required': 'este campo es obligatorio' },
		widget = forms.PasswordInput( attrs = { 'class': 'form-control', 'placeholder':'actual contraseña'} ),
		)

	password2 = forms.CharField( 
		label = "Nueva Contraseña",
		required = True,
		error_messages = { 'required': 'este campo es obligatorio' },
		widget = forms.PasswordInput( attrs = { 'class': 'form-control', 'type': 'password','placeholder':'nueva contraseña'} ),
		)

	class Meta:
		model = User
		fields = ('password1','password2')


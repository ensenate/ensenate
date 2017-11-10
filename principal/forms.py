# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm

from django.contrib.auth import get_user_model

from django.contrib.auth.tokens import default_token_generator

#modelo de usuario
from usuarios.models import User

#modelo de contactanos
from .models import Contacto

class crear_usuario_form(UserCreationForm):

	error_messages = {
	 	'password_mismatch': "las contraseñas no son iguales",
	}
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
	
	password1 = forms.CharField(
		label = "Contraseña",
		error_messages = { 'required': 'este campo es obligatorio' },
		widget = forms.PasswordInput( attrs = { 'class': 'form-control', 'placeholder':'ingresa tu contraseña'} ),
		)

	password2 = forms.CharField( 
		label = "Confirmar Contraseña",
		error_messages = { 'required': 'este campo es obligatorio' },
		widget = forms.PasswordInput(attrs={ 'class': 'form-control', 'type': 'password','placeholder':'confirma tu contraseña'} ),
		)

	class Meta:
		model = User
		fields = ('username','first_name','last_name','email', 'password1','password2')

class restablecer_password_form(PasswordResetForm):

	email = forms.CharField(
			label = "Correo Electronico",
			error_messages = { 'invalid':'ingresa un correo electronico valido', 'required': 'este campo es obligatorio' },
			widget = forms.TextInput( attrs = { 'class': 'form-control', 'type': 'email', 'placeholder':'ingresa tu correo electronico' } ),
			)

class contacto_form(forms.ModelForm):

	asunto= forms.CharField(
		label = "Asunto", 
		required = True,
		max_length = 50,
		error_messages = { 'unique': 'ya existe este usuario.',  'required': 'este campo es obligatorio' },
		widget = forms.TextInput( attrs = { 'class': 'form-control','placeholder':'ingresa tu asunto' } ),#se le puede poner todos los atributos del html
		)

	email = forms.CharField(
		label = "Correo Electronico",
		required = True,
		error_messages = { 'invalid':'ingresa un correo electronico valido', 'required': 'este campo es obligatorio' },
		widget = forms.TextInput( attrs = { 'class': 'form-control', 'type': 'email', 'placeholder':'ingresa tu correo electronico' } ),
		)

	
	mensaje = forms.CharField(
		label = "Mensaje",
		error_messages = { 'required': 'este campo es obligatorio' },
		widget = forms.Textarea(attrs={'class': 'form-control', 'type': 'text', 'placeholder':'ingresa tu mensaje'} ),
		)

	class Meta:
		model = Contacto
		fields = ('asunto','email','mensaje', )


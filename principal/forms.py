from django import forms
from django.contrib.auth.models import User

class crear_usuario_form(forms.ModelForm):

	error_messages = {
	 	'error_password': "las contraseñas no son iguales",
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
		fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

	def clean_password2(self):
		password1 = self.cleaned_data.get("password1")
		password2 = self.cleaned_data.get("password2")
		
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError(
			self.error_messages['error_password'],
			code='error_password',
			)
		return password2

	def save(self, commit=True):
		user = super().save(commit=False)
		user.set_password(self.cleaned_data["password1"])
		if commit:
			user.save()
		return user
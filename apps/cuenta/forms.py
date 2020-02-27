from django import forms
from apps.modelo.models import Persona

class DateInput(forms.DateInput):
	input_type = 'date'

class FormularioPersona(forms.ModelForm):
	class Meta:
		model = Persona
		fields = ["cedula","last_name","first_name", "edad", "fechaNacimiento", "direccion","telefono","username","password","email","rol"]
		labels = {
			'cedula':'Cedula',
			'last_name':'Apellidos',
			'first_name':'Nombres',
			'edad':'Edad',
			'fechaNacimiento':'Fecha de Nacimiento',
			'direccion':'Direccion',
			'telefono':'Telefono',
			"username":'Nombre de Usuario',
			"password":'Contraseña',
			"email":'Correo Electronico',
			'rol': 'Rol'
		}
		widgets = {
			'cedula':forms.TextInput(attrs={'class':'form-control','placeholder':'Cedula'}),
			'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Apellidos'}),
			'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Nombres'}),
			'edad':forms.TextInput(attrs={'class':'form-control','placeholder':'Edad','readonly':'readonly'}),
			'fechaNacimiento': DateInput(attrs={'class':'form-control'}),
			'direccion':forms.TextInput(attrs={'class':'form-control','placeholder':'Direccion'}),
			'telefono':forms.TextInput(attrs={'class':'form-control','placeholder':'Telefono'}),
			'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre de Usuario'}),
			'password':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Contraseña'}),
			'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Correo Electronico'}),
			'rol': forms.Select(attrs={'class':'form-control'}),#,'style':'visibility:hidden'}),
		}

class FormularioLogin(forms.Form):
	email = forms.CharField(widget = forms.TextInput(attrs={'class':'input-group form-control','placeholder':'Email'}),
								label='Usuario')
	clave = forms.CharField(widget = forms.PasswordInput(attrs={'class':'input-group form-control','placeholder':'Clave'}),
								label='Clave')
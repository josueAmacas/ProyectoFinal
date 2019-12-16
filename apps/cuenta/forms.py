from django import forms
from apps.modelo.models import Persona, Cuenta 

class DateInput(forms.DateInput):
	input_type = 'date'

class FormularioPersona(forms.ModelForm):
	class Meta:
		model = Persona
		fields = ["cedula", "apellidos",  "nombres", "edad", "fechaNacimiento", "direccion","telefono","rol"]
		labels = {
			'cedula':'Cedula',
			'apellidos':'Apellidos',
			'nombres':'Nombres',
			'edad':'Edad',
			'fechaNacimiento':'Fecha de Nacimiento',
			'direccion':'Direccion',
			'telefono':'Telefono',
			'rol': 'Rol'
		}
		widgets = {
			'cedula':forms.TextInput(attrs={'class':'form-control','placeholder':'Cedula'}),
			'apellidos':forms.TextInput(attrs={'class':'form-control','placeholder':'Apellidos'}),
			'nombres':forms.TextInput(attrs={'class':'form-control','placeholder':'Nombres'}),
			'edad':forms.TextInput(attrs={'class':'form-control','placeholder':'Edad','readonly':'readonly'}),
			'fechaNacimiento': DateInput(attrs={'class':'form-control'}),
			'direccion':forms.TextInput(attrs={'class':'form-control','placeholder':'Direccion'}),
			'telefono':forms.TextInput(attrs={'class':'form-control','placeholder':'Telefono'}),
			'rol': forms.Select(attrs={'class':'form-control', 'style':'visibility:hidden'}),
		}

class FormularioCuenta(forms.ModelForm):
	class Meta:
		model = Cuenta
		fields = ["correo", "clave"]
		labels = {
			'correo':'Correo Electronico',
			'clave':'Clave',
		}
		widgets = {
			'correo':forms.EmailInput(attrs={'class':'form-control','placeholder':'Corro Electronico'}),
			'clave':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Clave'}),
		}		

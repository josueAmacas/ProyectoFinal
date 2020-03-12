from django import forms
from apps.modelo.models import *

class DateInput(forms.DateInput):
	input_type = 'date'

class FormularioModificarRol(forms.ModelForm):
	class Meta:
		model = Persona
		fields = ["rol"]
		labels = {
			'rol': 'Rol'
		}
		widgets = {			
			'rol': forms.Select(attrs={'class':'form-control'}),
		}

class FormularioFoto(forms.ModelForm):
	class Meta:
		model = Persona
		fields = ["foto"]
		labels = {'foto': "Elejir Foto"}
		widgets ={'foto': forms.FileInput(attrs={'class': 'form-control'})}

class FormularioModificarPersona(forms.ModelForm):
	class Meta:
		model = Persona
		fields = ["last_name","first_name", "edad", "fechaNacimiento", "direccion","telefono"]
		labels = {
			'last_name':'Apellidos',
			'first_name':'Nombres',
			'edad':'Edad',
			'fechaNacimiento':'Fecha de Nacimiento',
			'direccion':'Direccion',
			'telefono':'Telefono',
		}
		widgets = {
			'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Apellidos'}),
			'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Nombres'}),
			'edad':forms.TextInput(attrs={'class':'form-control','placeholder':'Edad','readonly':'readonly'}),
			'fechaNacimiento': DateInput(attrs={'class':'form-control'}),
			'direccion':forms.TextInput(attrs={'class':'form-control','placeholder':'Direccion'}),
			'telefono':forms.TextInput(attrs={'class':'form-control','placeholder':'Telefono'}),
		}

class FormularioRSolicitud(forms.ModelForm):
	class Meta:
		model = Seguimiento	
		fields = ["revSolicitud",'tramite']
		labels = {
			'revSolicitud':'Solicitud',
		}
		widgets = {
			'revSolicitud':forms.CheckboxInput(attrs={'class':'form-control'}),	
			'tramite':forms.Select(attrs={'class':'form-control','style':'visibility:hidden'}),
		}

class FormularioAsigDocente(forms.ModelForm):
	class Meta:
		model = Seguimiento	
		fields = ["asigDocente",'tramite']
		labels = {
			'asigDocente':'Asignacion Docente',
		}
		widgets = {
			'asigDocente':forms.CheckboxInput(attrs={'class':'form-control'}),	
			'tramite':forms.Select(attrs={'class':'form-control','style':'visibility:hidden'}),	
		}

class FormularioADocente(forms.ModelForm):
	class Meta:
		model = Tramite	
		fields = ["docente",'registro']
		labels = {
			'docente':'Docente',
			'registro': 'Codigo',
		}
		widgets = {	
			'docente':forms.Select(attrs={'class':'form-control'}),
			'registro':forms.TextInput(attrs={'class':'form-control','readonly':'readonly'}),
		}

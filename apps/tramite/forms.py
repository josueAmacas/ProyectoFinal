from django import forms
from apps.modelo.models import *

class FormularioTramite(forms.ModelForm):
	class Meta:
		model = Tramite
		fields = ["registro","tipo","carrera"]
		labels = {
			'registro':'Codigo',
			'tipo':'Tipo',
			'carrera':'Carrera',
		}
		widgets = {
			'registro':forms.TextInput(attrs={'class':'form-control','readonly':'readonly'}),
			'tipo':forms.Select(attrs={'class':'form-control'}),
			'carrera':forms.Select(attrs={'class':'form-control'}),
		}


class FormularioArchivo(forms.ModelForm):
	class Meta:
		model = Archivo	
		fields = ["archivo"]
		labels = {
			'archivo':'Archivo',
		}
		widgets = {
			'archivo':forms.FileInput(attrs={'class':'form-control'}),	
		}

class FormularioRLegal(forms.ModelForm):
	class Meta:
		model = Seguimiento	
		fields = ["revSellos",'tramite']
		labels = {
			'revSellos':'Sellos',
		}
		widgets = {
			'revSellos':forms.CheckboxInput(attrs={'class':'form-control'}),	
			'tramite':forms.Select(attrs={'class':'form-control','style':'visibility:hidden'}),	
		}

class FormularioTEstado(forms.ModelForm):
	class Meta:
		model = Tramite
		fields = ["registro","estado"]
		labels = {
			'registro':'Codigo',
			'estado':'Estado',
		}
		widgets = {
			'registro':forms.TextInput(attrs={'class':'form-control','readonly':'readonly'}),
			'estado':forms.CheckboxInput(attrs={'class':'form-control'}),
		}

class FormularioInforme(forms.ModelForm):
	class Meta:
		model = Archivo	
		fields = ["informePeticionario"]
		labels = {
			'informePeticionario':'Informe Peticionario',
		}
		widgets = {
			'informePeticionario':forms.FileInput(attrs={'class':'form-control'}),	
		}

class FormularioRDocumentacion(forms.ModelForm):
	class Meta:
		model = Seguimiento
		fields = ["revDocumentacion",'tramite']
		labels = {
			'revDocumentacion':'Revicion Documentacion',
		}
		widgets = {
			'revDocumentacion':forms.CheckboxInput(attrs={'class':'form-control'}),	
			'tramite':forms.Select(attrs={'class':'form-control','style':'visibility:hidden'}),	
		}

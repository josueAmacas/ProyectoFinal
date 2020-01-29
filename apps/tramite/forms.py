from django import forms
from apps.modelo.models import Tramite, Carrera,Persona,Archivo

class Formulariotramite(forms.ModelForm):
	class Meta:
		model = Tramite
		fields = ["registro","tipo","external_carrera", "external_docente","archivo","persona"]
		labels = {
			'registro':'Codigo',
			'tipo':'Tipo',
			'external_carrera':'Carrera',
			'external_docente':'Docente',
			'archivo':'Archivo',
			'persona':'Persona',
		}
		widgets = {
			'registro':forms.TextInput(attrs={'class':'form-control','readonly':'readonly'}),
			'tipo':forms.Select(attrs={'class':'form-control'}),
			'external_carrera':forms.TextInput(attrs={'class':'form-control'}),
			'external_docente':forms.TextInput(attrs={'class':'form-control'}),
			'archivo':forms.Select(attrs={'class':'form-control'}),
			'persona':forms.Select(attrs={'class':'form-control'}),
		}


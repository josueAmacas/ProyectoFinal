from django import forms
from apps.modelo.models import Tramite, Carrera

class Formulariotramite(forms.ModelForm):
	class Meta:
		model = Tramite
		fields = ["registro","tipo", "carrera", "archivo","persona"]
		labels = {
			'registro':'Codigo',
			'tipo':'Tipo',
			'carrera':'Carrera',
			'archivo':'Archivo',
		}
		widgets = {
			'registro':forms.TextInput(attrs={'class':'form-control','readonly':'readonly'}),
			'tipo':forms.Select(attrs={'class':'form-control'}),
			'carrera':forms.Select(attrs={'class':'form-control'}),
			'archivo':forms.TextInput(attrs={'class':'form-control'}),
		}


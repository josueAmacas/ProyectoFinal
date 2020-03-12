from django import forms
from apps.modelo.models import *

class FormularioSilabo(forms.ModelForm):
	class Meta:
		model = Silabo
		fields = ["archivo","docente","materia","periodoAcademico"]
		labels = {
			'archivo': 'Archivo',
			'docente': 'Docente',
			'materia': 'Materia',
			'periodoAcademico': 'Periodo Academico',
		}
		widgets = {			
			
			'docente': forms.Select(attrs={'class':'form-control'}),
			'materia': forms.Select(attrs={'class':'form-control'}),
			'periodoAcademico': forms.Select(attrs={'class':'form-control'}),
		}

class FormularioEstadoSilabo(forms.ModelForm):
	class Meta:
		model = Silabo
		fields = ["estado","docente"]
		labels = {
			'estado': 'Estado',
			'docente': 'Docente',
		}
		widgets = {		
			'docente': forms.Select(attrs={'class':'form-control','readonly':'readonly'}),
			'estado':forms.CheckboxInput(attrs={'class':'form-control'}),	
		}
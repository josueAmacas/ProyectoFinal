from django import forms
from apps.modelo.models import *

class DateInput(forms.DateInput):
	input_type = 'date'

class FormularioPeriodoA(forms.ModelForm):
	class Meta:
		model = PeriodoAcademico
		fields = ["fechaInicio","fechaFin",'mallaCurricular']
		labels = {
			'fechaInicio':'Fecha Inicio',
			'fechaFin':'Fecha Fin',
			'mallaCurricular':'Malla Curricular'
		}
		widgets = {
			'fechaInicio': DateInput(attrs={'class':'form-control'}),
			'fechaFin': DateInput(attrs={'class':'form-control'}),
			'mallaCurricular': forms.Select(attrs={'class':'form-control'}),
		}

class FormularioEditarEstadoP(forms.ModelForm):
	class Meta:
		model = PeriodoAcademico
		fields = ["estado",'mallaCurricular']
		labels = {
			'estado':'Estado',
			'mallaCurricular':'Malla Curricular'
		}
		widgets = {
			'estado':forms.CheckboxInput(attrs={'class':'form-control'}),	
			'mallaCurricular': forms.Select(attrs={'class':'form-control'})#,'style':'visibility:hidden'}),
		}


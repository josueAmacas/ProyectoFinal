from django import forms
from apps.modelo.models import Rol, Persona

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
from django.shortcuts import render
from apps.modelo.models import Persona, Rol, Cuenta, Tramite, MallaCurricular, Carrera

def mallaSolicitante(request): 
	malla = MallaCurricular.objects.get(mallaCurricular_id = 1)
	context = {
		'malla':malla,
	}
	return render (request, 'solicitante/frm_malla.html', context)

def mallaDocente(request):
	malla = MallaCurricular.objects.get(mallaCurricular_id = 1)
	context = {
		'malla':malla,
	}
	return render (request, 'docente/frm_malla.html', context)

def mallaAbogado(request):
	malla = MallaCurricular.objects.get(mallaCurricular_id = 1)
	context = {
		'malla':malla,
	}
	return render (request, 'abogado/frm_malla.html', context)

def mallaDecano(request):
	malla = MallaCurricular.objects.all()
	context = {
		'lista': malla
	}
	return render (request, 'decano/frm_malla.html', context) 
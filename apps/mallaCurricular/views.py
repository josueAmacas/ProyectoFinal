from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.modelo.models import Persona, Rol, Tramite, MallaCurricular, Carrera

@login_required
def mallaSolicitante(request): 
	malla = MallaCurricular.objects.get(mallaCurricular_id = 1)
	persona = Persona.objects.get(cedula = request.user.cedula)
	context = {
		'malla':malla,
		'persona': persona,
	}
	return render (request, 'solicitante/frm_malla.html', context)

@login_required
def mallaDocente(request):
	malla = MallaCurricular.objects.get(mallaCurricular_id = 1)
	persona = Persona.objects.get(cedula = request.user.cedula)
	context = {
		'malla':malla,
		'persona': persona,
	}
	return render (request, 'docente/frm_malla.html', context)

@login_required
def mallaAbogado(request):
	malla = MallaCurricular.objects.get(mallaCurricular_id = 1)
	persona = Persona.objects.get(cedula = request.user.cedula)
	context = {
		'malla':malla,
		'persona': persona,
	}
	return render (request, 'abogado/frm_malla.html', context)

@login_required
def mallaDecano(request):
	malla = MallaCurricular.objects.all()
	m = MallaCurricular.objects.get(mallaCurricular_id = 1)
	persona = Persona.objects.get(cedula = request.user.cedula)
	context = {
		'malla':malla,
		'persona': persona,
		'm':m,
	}
	return render (request, 'decano/frm_malla.html', context) 
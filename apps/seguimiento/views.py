from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.modelo.models import *

@login_required
def seguimientoSolicitante(request):
	seguimiento = Seguimiento.objects.all()
	persona = Persona.objects.get(cedula = request.user.cedula)
	context = {
		'persona':persona,
		'seguimiento': seguimiento,
	}	
	return render (request, 'solicitante/frm_seguimiento.html',context)

@login_required
def seguimientoAbogado(request):
	persona = Persona.objects.get(cedula = request.user.cedula)
	seguimiento = Seguimiento.objects.all()
	context = {
		'persona':persona,
		'seguimiento':seguimiento,
	}	
	return render (request, 'abogado/frm_seguimiento.html',context)

@login_required
def seguimientoDocente(request):
	persona = Persona.objects.get(cedula = request.user.cedula)
	seguimiento = Seguimiento.objects.all()
	context = {
		'persona':persona,
		'seguimiento':seguimiento,
	}	
	return render (request, 'docente/frm_seguimiento.html',context)

@login_required
def seguimientoDecano(request):
	persona = Persona.objects.get(cedula = request.user.cedula)
	seguimiento = Seguimiento.objects.all()
	context = {
		'persona':persona,
		'seguimiento':seguimiento,
	}		
	return render (request, 'decano/frm_seguimiento.html',context)
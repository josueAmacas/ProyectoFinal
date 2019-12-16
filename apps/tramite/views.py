from django.shortcuts import render
from django.shortcuts import render, redirect
from apps.modelo.models import Persona, Rol, Cuenta, Tramite, Carrera

def tramiteSolicitante(request):
	return render (request, 'solicitante/frm_tramite.html')

def tramiteAbogado(request):
	return render (request, 'abogado/frm_tramite.html')

def tramiteDocente(request):
	return render (request, 'docente/frm_tramite.html')

def tramiteDecano(request):
	return render (request, 'decano/frm_tramite.html')
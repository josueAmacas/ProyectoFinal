from django.shortcuts import render, redirect
from apps.modelo.models import Persona, Rol, Cuenta, Tramite

def perfilSolicitante(request):
	return render (request, 'solicitante/frm_bienvenida.html')

def tramiteSolicitante(request):
	return render (request, 'solicitante/frm_tramite.html')

def seguimientoSolicitante(request):
	return render (request, 'solicitante/frm_seguimiento.html')

def mallaCurricular(request):
	return render (request, 'solicitante/frm_malla.html')

def requisitos(request):
	return render (request, 'solicitante/frm_requisitos.html')

def editarPerfil(request):
	return render (request, 'solicitante/frm_perfil.html')
	

def perfilDecano(request):
	return render (request, 'decano/frm_bienvenida.html')

def perfilAbogado(request):
	return render (request, 'abogado/frm_bienvenida.html')

def perfilDocente(request):
	return render (request, 'docente/frm_bienvenida.html')

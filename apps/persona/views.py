from django.shortcuts import render, redirect
from apps.modelo.models import Persona, Rol, Cuenta, Tramite, MallaCurricular, Carrera

def perfilSolicitante(request):
	return render (request, 'solicitante/frm_bienvenida.html')

def tramiteSolicitante(request):
	return render (request, 'solicitante/frm_tramite.html')

def seguimientoSolicitante(request):
	return render (request, 'solicitante/frm_seguimiento.html')

def mallaCurricular(request):
	malla = MallaCurricular.objects.get(mallaCurricular_id = 1)
	carrera = Carrera.objects.get(carrera_id = 1)
	context = {
		'malla':malla,
		'carrera':carrera,
	}
	return render (request, 'solicitante/frm_malla.html', context)

def requisitos(request):
	return render (request, 'solicitante/frm_requisitos.html')

def editarPerfil(request):
	return render (request, 'solicitante/frm_perfil.html')
	

def perfilDecano(request):
	return render (request, 'decano/frm_bienvenida.html')

def listaUsuarios(request):
	lista = Persona.objects.all()
	context ={
		'lista': lista,
	}
	return render (request, 'decano/frm_bienvenida.html')

def perfilAbogado(request):
	return render (request, 'abogado/frm_bienvenida.html')

def perfilDocente(request):
	return render (request, 'docente/frm_bienvenida.html')

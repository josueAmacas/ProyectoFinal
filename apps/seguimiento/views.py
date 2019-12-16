from django.shortcuts import render
from apps.modelo.models import Seguimiento

def seguimientoSolicitante(request):
	seguimiento = Seguimiento.objects.all()
	context = {
		'seguimiento': seguimiento,
	}	
	return render (request, 'solicitante/frm_seguimiento.html',context)

def seguimientoAbogado(request):
	
	return render (request, 'abogado/frm_seguimiento.html')

def seguimientoDocente(request):
	
	return render (request, 'docente/frm_seguimiento.html')

def seguimientoDecano(request):
	
	return render (request, 'decano/frm_seguimiento.html')
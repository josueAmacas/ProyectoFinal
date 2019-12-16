from django.shortcuts import render, redirect
from apps.modelo.models import Persona, Rol, Cuenta, Tramite, Carrera

def periodoAcademico(request):
	return render (request, 'decano/frm_periodo.html')
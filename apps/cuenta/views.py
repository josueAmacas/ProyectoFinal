from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
import json, crypt, os
from .forms import FormularioPersona
from apps.modelo.models import Persona
from django.contrib import messages

def ingresar(request):
	return render (request, 'login/frm_login.html')

def registro(request):
	formularioP = FormularioPersona(request.POST)
	if request.method == 'POST':
		if formularioP.is_valid():
			datosP = formularioP.cleaned_data
			persona = Persona()
			persona.password = datosP.get('password')
			persona.is_superuser = True
			persona.username = datosP.get("username")
			persona.first_name = datosP.get('first_name')
			persona.last_name = datosP.get('last_name')
			persona.email = datosP.get('email')
			persona.cedula = datosP.get('cedula')
			persona.edad = datosP.get('edad')
			persona.fechaNacimiento = datosP.get('fechaNacimiento')
			persona.direccion = datosP.get('direccion')
			persona.telefono = datosP.get('telefono')
			persona.foto = "sin_foto.jpg"
			persona.isDecano = True
			persona.isDocente = False
			persona.isEstudiante = False
			persona.isAbogado = False
			persona.rol = datosP.get('rol')
			persona.save()

			messages.success(request, "Creadocon exito")
			return redirect(ingresar)
	else:
		messages.error(request, 'Ha ocurrido un error!!')

	context = {
		'fPersona': formularioP
	}
	return render (request, 'login/frm_registro.html',context)

def cuentaUnica(request):
	
	dni = request.GET["cedula"]
	data ={
		Persona.objects.filter(cedula_iexact=cedula).exists()
	}
	return JsonResponse( data )
from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
import json, crypt, os
from .forms import FormularioPersona, FormularioCuenta
from apps.modelo.models import Persona,Cuenta
from django.contrib import messages

def ingresar(request):
	formularioC = FormularioCuenta()
	context = {
		'formulario': formularioC
	}
	return render (request, 'login/frm_login.html',context)

def registro(request):
	formularioP = FormularioPersona(request.POST)
	formularioC = FormularioCuenta(request.POST)
	if request.method == 'POST':
		if formularioP.is_valid() and formularioC.is_valid():
			datosP = formularioP.cleaned_data
			persona = Persona()
			persona.cedula = datosP.get('cedula')
			persona.apellidos = datosP.get('apellidos')
			persona.nombres = datosP.get('nombres')
			persona.edad = datosP.get('edad')
			persona.fechaNacimiento = datosP.get('fechaNacimiento')
			persona.telefono = datosP.get('telefono')
			persona.direccion = datosP.get('direccion')
			persona.foto = "sin_foto.jpg"
			persona.rol = datosP.get('rol')
			persona.save()

			datosC = formularioC.cleaned_data
			cuenta = Cuenta()
			cuenta.correo = datosC.get('correo')
			#clave = datosC.get('clave')
			#salt = os.environ.get('SALT')
			#cuenta.clave = crypt.crypt(clave,salt)
			cuenta.clave = datosC.get('clave')
			cuenta.persona = persona
			cuenta.save();
			messages.success(request, "Creadocon exito")
			return redirect(ingresar)
	else:
		messages.error(request, 'Ha ocurrido un error!!')

	context = {
		'fPersona': formularioP,
		'fCuenta': formularioC
	}
	return render (request, 'login/frm_registro.html', context)

def cuentaUnica(request):
	
	dni = request.GET["cedula"]
	data ={
		Persona.objects.filter(cedula_iexact=cedula).exists()
	}
	return JsonResponse( data )
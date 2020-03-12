import json, crypt, os
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from .forms import FormularioPersona, FormularioLogin
from apps.modelo.models import Persona

def ingresar(request):
	formulario = FormularioLogin(request.POST)
	if request.method == 'POST':
		if formulario.is_valid():
			email = request.POST.get('email')
			clave = request.POST.get('password')
			try:
				user =  Persona.objects.get(email = email)
				if user.check_password(clave):
					if user is not None:
						if user.is_active & user.isEstudiante:
							login(request, user)
							return HttpResponseRedirect(reverse('solicitante'))
						elif user.is_active & user.isDocente:
							login(request, user)
							return HttpResponseRedirect(reverse('docente'))
						elif user.is_active & user.isAbogado:
							login(request, user)
							return HttpResponseRedirect(reverse('abogado'))
						elif user.is_active & user.isDecano:
							login(request, user)
							return HttpResponseRedirect(reverse('decano'))
						else:
							messages.error(request,'Usuario descativado')
					else:
						messages.error(request,'Usuario y/o contrasena incorrectos')
				else:
					messages.error(request,'Usuario y/o contrasena incorrectos')
			except Exception as e:
				messages.error(request,'Usuario y/o contrasena incorrectos')
		
	else:
		formulario = FormularioLogin()
		

	context = {
		'formulario': formulario
	}
	return render (request, 'login/frm_login.html',context)

def registro(request):
	formularioP = FormularioPersona(request.POST)
	if request.method == 'POST':
		if formularioP.is_valid():
			datosP = formularioP.cleaned_data
			persona = Persona()
			persona.set_password(datosP.get("password"))
			persona.is_superuser = True
			persona.is_staff = True
			persona.username = datosP.get("username")
			persona.first_name = datosP.get('first_name')
			persona.last_name = datosP.get('last_name')
			persona.email = datosP.get('email')
			persona.cedula = datosP.get('cedula')
			persona.edad = datosP.get('edad')
			persona.fechaNacimiento = datosP.get('fechaNacimiento')
			persona.direccion = datosP.get('direccion')
			persona.telefono = datosP.get('telefono')
			persona.foto = "gallery/sin_foto.jpg"
			persona.isDecano = False
			persona.isDocente = False
			persona.isEstudiante = True
			persona.isAbogado = False
			persona.rol = datosP.get('rol')
			persona.save()

			messages.success(request, "Creado con exito")
			return redirect(ingresar)
		else:
			messages.error(request, 'Error...Cedula, Usuario o Correo ya existen!!')
	else:
		formularioP = FormularioPersona()
		

	context = {
		'fPersona': formularioP
	}
	return render (request, 'login/frm_registro.html',context)

def cerrar(request):
	logout(request)
	return HttpResponseRedirect(reverse('autenticar'))

	
def cuentaUnica(request):
	
	dni = request.GET["cedula"]
	data ={
		Persona.objects.filter(cedula_iexact=cedula).exists()
	}
	return JsonResponse( data )
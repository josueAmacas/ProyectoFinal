from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from django.conf import settings
from django.core.files.storage import FileSystemStorage
from apps.modelo.models import *
from .forms import *

@csrf_exempt
def cargarPersona(request):
	persona = Persona.objects.filter(cedula = request.POST.get('cedula',''))
	perObj = serializers.serialize('python',persona)
	return JsonResponse(perObj,safe=False)

@csrf_exempt
def cargarDocente(request):
	docente = Docente.objects.filter(docente_id = request.POST.get('docente_id',''))
	docObj = serializers.serialize('python',docente)
	return JsonResponse(docObj,safe=False)


#Vista perfiles
@login_required
def perfilSolicitante(request):
	persona = Persona.objects.get(cedula = request.user.cedula)
	context ={
		'persona': persona,
	}
	return render (request, 'solicitante/frm_bienvenida.html',context)

@login_required
def perfilDecano(request):
	persona = Persona.objects.get(cedula = request.user.cedula)
	context ={
		'persona': persona,
	}
	return render (request, 'decano/frm_bienvenida.html',context)

@login_required
def perfilAbogado(request):
	persona = Persona.objects.get(cedula = request.user.cedula)
	context ={
		'persona': persona,
	}
	return render (request, 'abogado/frm_bienvenida.html',context)

@login_required
def perfilDocente(request):
	persona = Persona.objects.get(cedula = request.user.cedula)
	context ={
		'persona': persona,
	}
	return render (request, 'docente/frm_bienvenida.html',context)

#Requisitos
@login_required
def requisitosSolicitante(request):
	persona = Persona.objects.get(cedula = request.user.cedula)
	context ={
		'persona': persona,
	}
	return render (request, 'solicitante/frm_requisitos.html',context)

@login_required
def requisitosDocente(request):
	persona = Persona.objects.get(cedula = request.user.cedula)
	context ={
		'persona': persona,
	}
	return render (request, 'docente/frm_requisitos.html',context)

@login_required
def requisitosAbogado(request):
	persona = Persona.objects.get(cedula = request.user.cedula)
	context ={
		'persona': persona,
	}
	return render (request, 'abogado/frm_requisitos.html',context)

@login_required
def requisitosDecano(request):
	persona = Persona.objects.get(cedula = request.user.cedula)
	context ={
		'persona': persona,
	}
	return render (request, 'decano/frm_requisitos.html',context)

#Editar Perfil
@login_required
def editarPerfilSolicitante(request):
	persona = Persona.objects.get(cedula = request.user.cedula)
	tramite = Tramite.objects.filter(persona_id = persona.persona_id)
	formularioEditar = FormularioModificarPersona(request.POST)
	if request.method == 'POST':
		if formularioEditar.is_valid():
			datosP = formularioEditar.cleaned_data
			persona.first_name = datosP.get('first_name')
			persona.last_name = datosP.get('last_name')
			persona.edad = datosP.get('edad')
			persona.fechaNacimiento = datosP.get('fechaNacimiento')
			persona.direccion = datosP.get('direccion')
			persona.telefono = datosP.get('telefono')
			persona.save()

			return redirect(editarPerfilSolicitante)
		else:
			print('Error en editar')
	else:
		print('formulario invalido')

	formFoto = FormularioFoto(request.POST,request.FILES)
	if request.method == 'POST':
		if formFoto.is_valid():
			datosF = formFoto.cleaned_data
			persona.foto = datosF.get('foto')
			persona.save()

			return redirect(editarPerfilSolicitante)
		else:
			print('Error en cargar foto')
	else:
		print('formulario invalido')

	context ={
		'persona': persona,
		'tramite': tramite,
		'frm':formularioEditar,
		'formF': formFoto,
	}
	return render (request, 'solicitante/frm_perfil.html',context)	

@login_required
def editarPerfilDocente(request):
	persona = Persona.objects.get(cedula = request.user.cedula)
	formularioEditar = FormularioModificarPersona(request.POST)
	if request.method == 'POST':
		if formularioEditar.is_valid():
			datosP = formularioEditar.cleaned_data
			persona.first_name = datosP.get('first_name')
			persona.last_name = datosP.get('last_name')
			persona.edad = datosP.get('edad')
			persona.fechaNacimiento = datosP.get('fechaNacimiento')
			persona.direccion = datosP.get('direccion')
			persona.telefono = datosP.get('telefono')
			persona.save()

			return redirect(editarPerfilDocente)
		else:
			print('Error en editar')
	else:
		print('formulario invalido')

	formFoto = FormularioFoto(request.POST,request.FILES)
	if request.method == 'POST':
		if formFoto.is_valid():
			datosF = formFoto.cleaned_data
			persona.foto = datosF.get('foto')
			persona.save()

			return redirect(editarPerfilDocente)
		else:
			print('Error en cargar foto')
	else:
		print('formulario invalido')
	context ={
		'persona': persona,
		'frm':formularioEditar,
		'formF': formFoto,
	}
	return render (request, 'docente/frm_perfil.html',context)

@login_required
def editarPerfilAbogado(request):
	persona = Persona.objects.get(cedula = request.user.cedula)
	formularioEditar = FormularioModificarPersona(request.POST)
	if request.method == 'POST':
		if formularioEditar.is_valid():
			datosP = formularioEditar.cleaned_data
			persona.first_name = datosP.get('first_name')
			persona.last_name = datosP.get('last_name')
			persona.edad = datosP.get('edad')
			persona.fechaNacimiento = datosP.get('fechaNacimiento')
			persona.direccion = datosP.get('direccion')
			persona.telefono = datosP.get('telefono')
			persona.save()

			return redirect(editarPerfilAbogado)
		else:
			print('Error en editar')
	else:
		print('formulario invalido')

	formFoto = FormularioFoto(request.POST,request.FILES)
	if request.method == 'POST':
		if formFoto.is_valid():
			datosF = formFoto.cleaned_data
			persona.foto = datosF.get('foto')
			persona.save()

			return redirect(editarPerfilAbogado)
		else:
			print('Error en cargar foto')
	else:
		print('formulario invalido')
	context ={
		'persona': persona,
		'frm':formularioEditar,
		'formF': formFoto,
	}
	return render (request, 'abogado/frm_perfil.html',context)

@login_required
def editarPerfilDecano(request):
	persona = Persona.objects.get(cedula = request.user.cedula)
	formularioEditar = FormularioModificarPersona(request.POST)
	if request.method == 'POST':
		if formularioEditar.is_valid():
			datosP = formularioEditar.cleaned_data
			persona.first_name = datosP.get('first_name')
			persona.last_name = datosP.get('last_name')
			persona.edad = datosP.get('edad')
			persona.fechaNacimiento = datosP.get('fechaNacimiento')
			persona.direccion = datosP.get('direccion')
			persona.telefono = datosP.get('telefono')
			persona.save()

			return redirect(editarPerfilDecano)
		else:
			print('Error en editar')
	else:
		print('formulario invalido')

	formFoto = FormularioFoto(request.POST,request.FILES)
	if request.method == 'POST':
		if formFoto.is_valid():
			datosF = formFoto.cleaned_data
			persona.foto = datosF.get('foto')
			persona.save()

			return redirect(editarPerfilDecano)
		else:
			print('Error en cargar foto')
	else:
		print('formulario invalido')
	context ={
		'persona': persona,
		'frm':formularioEditar,
		'formF': formFoto,
	}
	return render (request, 'decano/frm_perfil.html',context)

#funciones del Decano(Admin)
@login_required
def listaUsuarios(request):
	lista = Persona.objects.all()
	rol = Rol.objects.all()
	persona = Persona.objects.get(cedula = request.user.cedula)
	fModificarRol = FormularioModificarRol(request.POST)
	context ={
		'lista': lista,
		'rol':rol,
		'persona':persona,
		'formulario': fModificarRol,
	}
	return render (request, 'decano/frm_usuarios.html', context)

@login_required
def listaDocentes(request):
	lista = Docente.objects.all()
	cd = Carrera.objects.get(carrera_id = 1)
	persona = Persona.objects.get(cedula = request.user.cedula)
	context ={
		'persona':persona,
		'lista': lista,
		'cd': cd,
	}
	return render (request, 'decano/frm_docente.html',context)

@login_required
def asignacionesDecano(request):
	persona = Persona.objects.get(cedula = request.user.cedula)
	seguimiento = Seguimiento.objects.all()
	frmA = FormularioAsigDocente(request.POST)
	frmD = FormularioADocente(request.POST)
	if request.method == 'POST':
		if frmA.is_valid() and frmD.is_valid():
			datosS = frmA.cleaned_data
			sid = datosS.get('tramite')
			seg = Seguimiento.objects.get(tramite_id = sid)
			seg.asigDocente = datosS.get('asigDocente')
			seg.save()

			datosT = frmD.cleaned_data			
			reg = datosT.get('registro')
			tramite = Tramite.objects.get(registro = reg)
			tramite.docente = datosT.get('docente')
			tramite.save()
			return redirect(asignacionesDecano)
		else:
			print("Formulario Solicitudes no valido")
	else:
		print("Error en formulario Revision Solicitudes")

	context ={
		'persona': persona,
		'seguimiento':seguimiento,
		'frmA':frmA,
		'frmD':frmD,
	}
	return render (request, 'decano/frm_asignacion.html',context)

@login_required
def solicitudesDecano(request):
	persona = Persona.objects.get(cedula = request.user.cedula)
	seguimiento = Seguimiento.objects.all()
	frmSol = FormularioRSolicitud(request.POST)
	if request.method == 'POST':
		if frmSol.is_valid():
			datosS = frmSol.cleaned_data
			sid = datosS.get('tramite')
			seg = Seguimiento.objects.get(tramite_id = sid)
			seg.revSolicitud = datosS.get('revSolicitud')
			seg.save()
			return redirect(solicitudesDecano)
		else:
			print("Formulario Solicitudes no valido")
	else:
		print("Error en formulario Revision Solicitudes")


	context ={
		'seguimiento': seguimiento,
		'persona': persona,
		'frmSol': frmSol,
	}
	return render (request, 'decano/frm_solicitudes.html',context)

#Plan de estudios
@login_required
def planDecano(request):
	carrera = Carrera.objects.get(carrera_id = 1)
	malla = MallaCurricular.objects.get(mallaCurricular_id = 1)
	ciclo1 = Materia.objects.filter(ciclo_id = 1)
	ciclo2 = Materia.objects.filter(ciclo_id = 2)
	ciclo3 = Materia.objects.filter(ciclo_id = 3)
	ciclo4 = Materia.objects.filter(ciclo_id = 4)
	ciclo5 = Materia.objects.filter(ciclo_id = 5)
	ciclo6 = Materia.objects.filter(ciclo_id = 6)
	ciclo7 = Materia.objects.filter(ciclo_id = 7)
	ciclo8 = Materia.objects.filter(ciclo_id = 8)
	ciclo9 = Materia.objects.filter(ciclo_id = 9)
	ciclo10 = Materia.objects.filter(ciclo_id = 10)
	n1 = Ciclo.objects.get(ciclo_id = 1)
	n2 = Ciclo.objects.get(ciclo_id = 2)
	n3 = Ciclo.objects.get(ciclo_id = 3)
	n4 = Ciclo.objects.get(ciclo_id = 4)
	n5 = Ciclo.objects.get(ciclo_id = 5)
	n6 = Ciclo.objects.get(ciclo_id = 6)
	n7 = Ciclo.objects.get(ciclo_id = 7)
	n8 = Ciclo.objects.get(ciclo_id = 8)
	n9 = Ciclo.objects.get(ciclo_id = 9)
	n10 = Ciclo.objects.get(ciclo_id = 10)
	persona = Persona.objects.get(cedula = request.user.cedula)
	context = {
		'carrera':carrera,
		'malla':malla,
		'ciclo1':ciclo1,
		'ciclo2':ciclo2,
		'ciclo3':ciclo3,
		'ciclo4':ciclo4,
		'ciclo5':ciclo5,
		'ciclo6':ciclo6,
		'ciclo7':ciclo7,
		'ciclo8':ciclo8,
		'ciclo9':ciclo9,
		'ciclo10':ciclo10,
		'n1': n1,
		'n2': n2,
		'n3': n3,
		'n4': n4,
		'n5': n5,
		'n6': n6,
		'n7': n7,
		'n8': n8,
		'n9': n9,
		'n10': n10,
		'persona':persona
	}
	return render (request, 'decano/frm_plan.html',context)

@login_required
def planAbogado(request):
	carrera = Carrera.objects.get(carrera_id = 1)
	malla = MallaCurricular.objects.get(mallaCurricular_id = 1)
	ciclo1 = Materia.objects.filter(ciclo_id = 1)
	ciclo2 = Materia.objects.filter(ciclo_id = 2)
	ciclo3 = Materia.objects.filter(ciclo_id = 3)
	ciclo4 = Materia.objects.filter(ciclo_id = 4)
	ciclo5 = Materia.objects.filter(ciclo_id = 5)
	ciclo6 = Materia.objects.filter(ciclo_id = 6)
	ciclo7 = Materia.objects.filter(ciclo_id = 7)
	ciclo8 = Materia.objects.filter(ciclo_id = 8)
	ciclo9 = Materia.objects.filter(ciclo_id = 9)
	ciclo10 = Materia.objects.filter(ciclo_id = 10)
	n1 = Ciclo.objects.get(ciclo_id = 1)
	n2 = Ciclo.objects.get(ciclo_id = 2)
	n3 = Ciclo.objects.get(ciclo_id = 3)
	n4 = Ciclo.objects.get(ciclo_id = 4)
	n5 = Ciclo.objects.get(ciclo_id = 5)
	n6 = Ciclo.objects.get(ciclo_id = 6)
	n7 = Ciclo.objects.get(ciclo_id = 7)
	n8 = Ciclo.objects.get(ciclo_id = 8)
	n9 = Ciclo.objects.get(ciclo_id = 9)
	n10 = Ciclo.objects.get(ciclo_id = 10)
	persona = Persona.objects.get(cedula = request.user.cedula)
	
	context = {
		'persona': persona,
		'carrera':carrera,
		'malla':malla,
		'ciclo1':ciclo1,
		'ciclo2':ciclo2,
		'ciclo3':ciclo3,
		'ciclo4':ciclo4,
		'ciclo5':ciclo5,
		'ciclo6':ciclo6,
		'ciclo7':ciclo7,
		'ciclo8':ciclo8,
		'ciclo9':ciclo9,
		'ciclo10':ciclo10,
		'n1': n1,
		'n2': n2,
		'n3': n3,
		'n4': n4,
		'n5': n5,
		'n6': n6,
		'n7': n7,
		'n8': n8,
		'n9': n9,
		'n10': n10,
	}
	return render (request, 'abogado/frm_plan.html',context)

@login_required
def planDocente(request):
	carrera = Carrera.objects.get(carrera_id = 1)
	malla = MallaCurricular.objects.get(mallaCurricular_id = 1)
	ciclo1 = Materia.objects.filter(ciclo_id = 1)
	ciclo2 = Materia.objects.filter(ciclo_id = 2)
	ciclo3 = Materia.objects.filter(ciclo_id = 3)
	ciclo4 = Materia.objects.filter(ciclo_id = 4)
	ciclo5 = Materia.objects.filter(ciclo_id = 5)
	ciclo6 = Materia.objects.filter(ciclo_id = 6)
	ciclo7 = Materia.objects.filter(ciclo_id = 7)
	ciclo8 = Materia.objects.filter(ciclo_id = 8)
	ciclo9 = Materia.objects.filter(ciclo_id = 9)
	ciclo10 = Materia.objects.filter(ciclo_id = 10)
	n1 = Ciclo.objects.get(ciclo_id = 1)
	n2 = Ciclo.objects.get(ciclo_id = 2)
	n3 = Ciclo.objects.get(ciclo_id = 3)
	n4 = Ciclo.objects.get(ciclo_id = 4)
	n5 = Ciclo.objects.get(ciclo_id = 5)
	n6 = Ciclo.objects.get(ciclo_id = 6)
	n7 = Ciclo.objects.get(ciclo_id = 7)
	n8 = Ciclo.objects.get(ciclo_id = 8)
	n9 = Ciclo.objects.get(ciclo_id = 9)
	n10 = Ciclo.objects.get(ciclo_id = 10)
	persona = Persona.objects.get(cedula = request.user.cedula)

	context = {
		'persona': persona,
		'carrera':carrera,
		'malla':malla,
		'ciclo1':ciclo1,
		'ciclo2':ciclo2,
		'ciclo3':ciclo3,
		'ciclo4':ciclo4,
		'ciclo5':ciclo5,
		'ciclo6':ciclo6,
		'ciclo7':ciclo7,
		'ciclo8':ciclo8,
		'ciclo9':ciclo9,
		'ciclo10':ciclo10,
		'n1': n1,
		'n2': n2,
		'n3': n3,
		'n4': n4,
		'n5': n5,
		'n6': n6,
		'n7': n7,
		'n8': n8,
		'n9': n9,
		'n10': n10,
	}
	return render (request, 'docente/frm_plan.html',context)

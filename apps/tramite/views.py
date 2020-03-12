from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from apps.modelo.models import *
from .forms import *

@login_required
def tramiteSolicitante(request):
	persona = Persona.objects.get(cedula = request.user.cedula)
	codigo = "TME - 00" + (str(len(Tramite.objects.all()) +1))
	tramite = Tramite.objects.filter(persona_id = persona.persona_id)
	carrera = Carrera.objects.all()
	docente = Docente.objects.get(docente_id = 1)
	frmTram = FormularioTramite(request.POST)
	frmArch = FormularioArchivo(request.POST, request.FILES)
	if request.method == 'POST':
		if frmArch.is_valid() and frmTram.is_valid():
			datosA = frmArch.cleaned_data
			archivo =Archivo()
			archivo.archivo = datosA.get('archivo')
			archivo.save()

			datosT = frmTram.cleaned_data
			tramite = Tramite()
			tramite.registro = datosT.get('registro')
			tramite.estado = False
			tramite.tipo = datosT.get('tipo')
			tramite.archivo = archivo
			tramite.carrera = datosT.get('carrera')
			tramite.docente = docente
			tramite.persona = persona
			tramite.save()

			seguimiento = Seguimiento()
			seguimiento.revSolicitud = False
			seguimiento.revSellos = False
			seguimiento.asigDocente = False
			seguimiento.revDocumentacion = False
			seguimiento.tramite = tramite
			seguimiento.save()

			return redirect(tramiteSolicitante)

		else:
			print('Error agregar')
	else:
		print('Error en formularios')


	context ={
		'persona': persona,
		'codigo': codigo,
		'carrera':carrera,
		'tramite': tramite,
		'frmA':frmArch,
		'frmT':frmTram,
	}
	return render (request, 'solicitante/frm_tramite.html',context)

@login_required
def tramiteAbogado(request):
	persona = Persona.objects.get(cedula = request.user.cedula)
	tramite = Seguimiento.objects.all()
	frmSellos = FormularioRLegal(request.POST)
	if request.method == 'POST':
		if frmSellos.is_valid():
			datosS = frmSellos.cleaned_data
			sid = datosS.get('tramite')
			seg = Seguimiento.objects.get(tramite_id = sid)
			seg.revSellos = datosS.get('revSellos')
			seg.save()
			return redirect(tramiteAbogado)
		else:
			print("Formulario Sellos no valido")
	else:
		print("Error en formulario Revision Sellos")
	context ={
		'persona': persona,
		'tramite':tramite,
		'frm':frmSellos,
	}
	return render (request, 'abogado/frm_tramite.html',context)

@login_required
def tramiteDocente(request):
	persona = Persona.objects.get(cedula = request.user.cedula)
	tramite = Seguimiento.objects.all()

	frmDoc = FormularioRDocumentacion(request.POST)
	if request.method == 'POST':
		if frmDoc.is_valid():
			datosD = frmDoc.cleaned_data
			sid = datosD.get('tramite')
			seg = Seguimiento.objects.get(tramite_id = sid)
			seg.revDocumentacion = datosD.get('revDocumentacion')
			seg.save()
			return redirect(tramiteDocente)
		else:
			print("Formulario Revision Documentacion no valido")
	else:
		print("Error en formulario Revision Documentacion")

	frmT = FormularioTramite(request.POST)
	frmInf = FormularioInforme(request.POST, request.FILES)
	if request.method == 'POST':
		if frmInf.is_valid() and frmT.is_valid():
			datosT = frmT.cleaned_data
			idT = datosT.get('tramite')
			tramit = Tramite.objects.get(registro = idT)
			print(tramit)
			arch = Archivo.objects.get(id_archivo = tramit.archivo)
			print(arch)

			datosD = frmInf.cleaned_data
			arch.informePeticionario = datosD.get('informePeticionario')
			seg.save()
			return redirect(tramiteDocente)
		else:
			print("Formulario Informe no valido")
	else:
		print("Error en formulario Informe Peticionario")

	context ={
		'persona': persona,
		'tramite':tramite,
		'frmDoc':frmDoc,
		'frmInf':frmInf,
		'frmT':frmT,
	}

	return render (request, 'docente/frm_tramite.html',context)

@login_required
def tramiteDecano(request):
	persona = Persona.objects.get(cedula = request.user.cedula)
	tramite = Tramite.objects.all()
	frmET = FormularioTEstado(request.POST)
	if request.method == 'POST':
		if frmET.is_valid():
			datosT = frmET.cleaned_data
			reg = datosT.get('registro')
			tramite = Tramite.objects.get(registro = reg)
			tramite.estado = datosT.get('estado')
			tramite.save()

			return redirect(tramiteDecano)
		else:
			print("Formulario Sellos no valido")
	else:
		print("Error en formulario Revision Sellos")

	context ={
		'persona': persona,
		'tramite':tramite,
		'frmET':frmET,
	}
	return render (request, 'decano/frm_tramite.html',context)
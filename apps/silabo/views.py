from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from apps.modelo.models import *
from .forms import *

#Vista perfiles
@login_required
def silaboDecano(request):
	silabo = Silabo.objects.all()
	persona = Persona.objects.get(cedula = request.user.cedula)	
	frmEstadoSilabo = FormularioEstadoSilabo(request.POST)
	if request.method == 'POST':
		if frmEstadoSilabo.is_valid():
			datos = frmEstadoSilabo.cleaned_data
			doc = datos.get('docente')
			silabo = Silabo.objects.get(docente_id = doc)
			silabo.estado = datos.get('estado')
			silabo.save()

			return redirect(silaboDecano)
		else:
			print("Error al modificar silabo")
	else:
		print("Error en el formulario Estado Silabo")

	context = {
		'silabo': silabo,
		'persona':persona,
		'frmES': frmEstadoSilabo,
	}
	return render (request, 'decano/frm_silabos.html', context)

@login_required
def silaboDocente(request):
	silabo = Silabo.objects.all()
	persona = Persona.objects.get(cedula = request.user.cedula)
	periodo = PeriodoAcademico.objects.all()
	materia = Materia.objects.all()
	formulario = FormularioSilabo(request.POST,request.FILES)
	if request.method == 'POST':
		if formulario.is_valid():
			datos = formulario.cleaned_data 
			silabo = Silabo()
			silabo.estado = True
			silabo.archivo =  datos.get('archivo')
			silabo.docente = 3 #persona.persona_id
			silabo.materia = datos.get("materia")
			silabo.periodoAcademico = datos.get("periodoAcademico")
			silabo.save()
			
			messages.success(request, "Creadocon exito")
			return redirect(silaboDocente)
		else:
			print("Error")
	else:
		formulario = FormularioSilabo()
		print("Error  2")

	context = {
		'silabo': silabo,
		'persona': persona,
		'periodo':periodo,
		'materia': materia,
		'form':formulario
	}
	return render (request, 'docente/frm_silabos.html', context)
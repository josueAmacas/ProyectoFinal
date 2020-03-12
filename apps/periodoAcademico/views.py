from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from apps.modelo.models import *
from .forms import *

@login_required
def periodoAcademico(request):
	periodo = PeriodoAcademico.objects.all()
	persona = Persona.objects.get(cedula = request.user.cedula)
	malla = MallaCurricular.objects.get(mallaCurricular_id = 1)

	frmP = FormularioPeriodoA(request.POST)
	if request.method == 'POST':
		if frmP.is_valid():
			datosP = frmP.cleaned_data
			periodoA = PeriodoAcademico()
			periodoA.fechaInicio = datosP.get('fechaInicio')
			periodoA.fechaFin = datosP.get('fechaFin')
			periodoA.estado = True 
			periodoA.mallaCurricular =datosP.get('mallaCurricular')
			periodoA.save()

			return redirect(periodoAcademico)
		else:
			print('Error en agregar Periodo')
	else:
		print('formulario invalido')

	context = {
		'periodo': periodo,
		'malla': malla,
		'persona':persona,
		'frmP':frmP,
	}
	return render (request, 'decano/frm_periodo.html', context)
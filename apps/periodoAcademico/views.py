from django.shortcuts import render, redirect
from apps.modelo.models import PeriodoAcademico, MallaCurricular

def periodoAcademico(request):
	periodo = PeriodoAcademico.objects.all()
	malla = MallaCurricular.objects.get(mallaCurricular_id = 1)
	context = {
		'periodo': periodo,
		'malla': malla,
	}
	return render (request, 'decano/frm_periodo.html', context)
from django.shortcuts import render, redirect
from apps.modelo.models import Tramite, Carrera, Docente, Silabo

#Vista perfiles
def silaboDecano(request):
	silabo = Silabo.objects.all()
	context = {
		'silabo': silabo,
	}
	return render (request, 'decano/frm_silabos.html', context)

def silaboDocente(request):
	silabo = Silabo.objects.all()
	context = {
		'silabo': silabo,
	}
	return render (request, 'docente/frm_silabos.html', context)
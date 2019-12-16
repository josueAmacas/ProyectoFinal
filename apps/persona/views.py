from django.shortcuts import render, redirect
from apps.modelo.models import Persona, Rol, Cuenta, Tramite, Carrera, Docente, MallaCurricular,Materia, Ciclo
from .forms import FormularioModificarRol

#Vista perfiles
def perfilSolicitante(request):
	return render (request, 'solicitante/frm_bienvenida.html')

def perfilDecano(request):
	return render (request, 'decano/frm_bienvenida.html')

def perfilAbogado(request):
	return render (request, 'abogado/frm_bienvenida.html')

def perfilDocente(request):
	return render (request, 'docente/frm_bienvenida.html')

#Requisitos
def requisitosSolicitante(request):
	return render (request, 'solicitante/frm_requisitos.html')

def requisitosDocente(request):
	return render (request, 'docente/frm_requisitos.html')

def requisitosAbogado(request):
	return render (request, 'abogado/frm_requisitos.html')

def requisitosDecano(request):
	return render (request, 'decano/frm_requisitos.html')

#Editar Perfil
def editarPerfil(request):
	return render (request, 'solicitante/frm_perfil.html')	



#funciones del Decano(Admin)
def listaUsuarios(request):
	lista = Cuenta.objects.all()
	rol = Rol.objects.all()
	fModificarRol = FormularioModificarRol(request.POST)
	context ={
		'lista': lista,
		'rol':rol,
		'formulario': fModificarRol,
	}
	return render (request, 'decano/frm_usuarios.html', context)

def listaDocentes(request):
	lista = Docente.objects.all()
	cd = Carrera.objects.get(external_id = "951600b31ddc11eabc845a5fcce30b8c")
	context ={
		'lista': lista,
		'cd': cd,
	}
	return render (request, 'decano/frm_docente.html',context)

def asignacionesDecano(request):
	return render (request, 'decano/frm_asignacion.html')

def solicitudesDecano(request):
	return render (request, 'decano/frm_solicitudes.html')

#Plan de estudios
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
	}
	return render (request, 'decano/frm_plan.html',context)

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
	}
	return render (request, 'abogado/frm_plan.html',context)

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
	}
	return render (request, 'docente/frm_plan.html',context)

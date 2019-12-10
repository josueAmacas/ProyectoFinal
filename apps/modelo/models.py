import uuid
from django.db import models

class Carrera(models.Model):
	carrera_id = models.AutoField(primary_key = True)
	area = models.CharField(max_length=150, null=False)
	nombre = models.CharField(max_length=50, null=False)
	external_id = models.UUIDField(default= uuid.uuid4, editable= False)

	def __str__(self):
		return '{}'.format(self.nombre)

class MallaCurricular(models.Model):
	mallaCurricular_id = models.AutoField(primary_key = True)
	archivo = models.CharField(max_length=200, null= False)
	anio =  models.CharField(max_length = 5, null = False)
	estado = models.BooleanField(default =True)
	external_id = models.UUIDField(default= uuid.uuid4, editable= False)
	carrera = models.ForeignKey(
		'Carrera', 
		on_delete = models.CASCADE,
	)

class Ciclo(models.Model):
	ciclo_id = models.AutoField(primary_key = True)
	numero = models.CharField(max_length = 3, null = False)
	nombre = models.CharField(max_length = 50, null = False)
	mallaCurricular = models.ForeignKey(
		'MallaCurricular', 
		on_delete = models.CASCADE,
	)

class Materia(models.Model):
	materia_id = models.AutoField(primary_key = True)
	nombre = models.CharField(max_length=50, null=False)
	creditos = models.CharField(max_length=10, null=False)
	codigo = models.CharField(max_length=50, null=False)
	duracion = models.CharField(max_length=10, null=False)
	obligatoria = models.CharField(max_length=10, null=False)
	external_id = models.UUIDField(default= uuid.uuid4, editable= False)
	ciclo = models.ForeignKey(
		'Ciclo', 
		on_delete = models.CASCADE,
	)

class PeriodoAcademico(models.Model):
	periodoAcademico_id = models.AutoField(primary_key = True)
	fechaInicio = models.DateField(auto_now = False, auto_now_add = False, null = False)
	fechaFin = models.DateField(auto_now = False, auto_now_add = False, null = False)
	estado = models.BooleanField(default =True)
	external_id = models.UUIDField(default= uuid.uuid4, editable= False)

class Rol(models.Model):
	listaRol =(
		('decano', 'Decano'),
		('abogado', 'Abogado'),
		('docente', 'Docente'),
		('solicitante', 'Solicitante'),
	)
	rol_id = models.AutoField(primary_key = True)
	nombre = models.CharField(max_length=20, choices = listaRol, default='Solicitante', null= False)

	def __str__(self):
		return '{}'.format(self.nombre)


class Persona(models.Model):
	persona_id = models.AutoField(primary_key = True)
	cedula = models.CharField(max_length=10, unique = True, null=False)
	apellidos = models.CharField(max_length=50, null=False)
	nombres = models.CharField(max_length=50, null=False)
	edad = models.CharField(max_length=3, null=False)
	fechaNacimiento =  models.DateField(auto_now = False, auto_now_add = False, null = False)
	direccion = models.TextField(max_length=50, default= 'sin direccion')
	telefono = models.CharField(max_length=13)
	foto = models.CharField(max_length=200)
	external_id = models.UUIDField(default= uuid.uuid4, editable= False)
	rol = models.ForeignKey(
		'Rol', 
		on_delete = models.CASCADE,
	)

class Docente(models.Model):
	docente_id = models.AutoField(primary_key = True)
	titulo = models.CharField(max_length=50, null=False)
	carrera = models.CharField(max_length=50, null=False)
	external_id = models.UUIDField(default= uuid.uuid4, editable= False)
	persona = models.ForeignKey(
		'Persona', 
		on_delete = models.CASCADE,
	)
	
class Cuenta(models.Model):
	cuenta_id = models.AutoField(primary_key = True)
	correo = models.EmailField(max_length = 50, null = False)
	clave = models.CharField(max_length = 50, null = False)
	estado = models.BooleanField(default =True)	
	external_id = models.UUIDField(default= uuid.uuid4, editable= False)
	persona = models.ForeignKey(
		'Persona', 
		on_delete = models.CASCADE,
	)

class Silabo(models.Model):
	Silabo_id = models.AutoField(primary_key = True)
	estado = models.BooleanField(default =True)
	archivo = models.CharField(max_length = 200, null = False)
	external_id = models.UUIDField(default= uuid.uuid4, editable= False)
	docente = models.ForeignKey(
		'Docente', 
		on_delete = models.CASCADE,
	)
	materia = models.ForeignKey(
		'Materia', 
		on_delete = models.CASCADE,
	)
	periodoAcademico = models.ForeignKey(
		'PeriodoAcademico', 
		on_delete = models.CASCADE,
	)

class Archivo(models.Model):
	archivo_id = models.AutoField(primary_key = True)
	archivo = models.CharField(max_length = 200, null = False)
	informePeticionario = models.CharField(max_length = 200, null = False)
	external_id = models.UUIDField(default= uuid.uuid4, editable= False)

class Tramite(models.Model):
	tramite_id = models.AutoField(primary_key = True)
	registro = models.CharField(max_length = 200, null = False)
	estado = models.BooleanField(default =False)
	external_docente = models.CharField(max_length = 200, null = False)
	external_carrera = models.CharField(max_length = 200, null = False)
	tipo = models.CharField(max_length = 200, null = False)
	external_id = models.UUIDField(default= uuid.uuid4, editable= False)
	archivo = models.ForeignKey(
		'Archivo', 
		on_delete = models.CASCADE,
	)
	persona = models.ForeignKey(
		'Persona', 
		on_delete = models.CASCADE,
	)

class Seguimiento(models.Model):
	seguimiento_id = models.AutoField(primary_key = True)
	revSolicitud = models.BooleanField(default =False)
	revSellos = models.BooleanField(default =False)
	asigDocente = models.BooleanField(default =False)
	revDocumentacion = models.BooleanField(default =False)
	external_id = models.UUIDField(default= uuid.uuid4, editable= False)
	tramite =  models.ForeignKey(
		'Tramite', 
		on_delete = models.CASCADE,
	)

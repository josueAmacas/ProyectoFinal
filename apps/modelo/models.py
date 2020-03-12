from django.db import models
from django.contrib.auth.models import AbstractUser

class Carrera(models.Model):
	carrera_id = models.AutoField(primary_key = True)
	area = models.CharField(max_length=200, null=False)
	nombre = models.CharField(max_length=200, null=False)

	def __str__(self):
		return '{}'.format(self.nombre)

class MallaCurricular(models.Model):
	mallaCurricular_id = models.AutoField(primary_key = True)
	archivo = models.FileField(upload_to='mallas', null= False)
	anio =  models.CharField(max_length = 5, null = False)
	estado = models.BooleanField(default =True)
	carrera = models.ForeignKey(
		'Carrera', 
		on_delete = models.CASCADE,
	)

	def __str__(self):
		return '{}{}'.format("Malla Curricular  ",self.anio)

class Ciclo(models.Model):
	ciclo_id = models.AutoField(primary_key = True)
	numero = models.CharField(max_length = 3, null = False)
	nombre = models.CharField(max_length = 200, null = False)
	mallaCurricular = models.ForeignKey(
		'MallaCurricular', 
		on_delete = models.CASCADE,
	)

class Materia(models.Model):
	materia_id = models.AutoField(primary_key = True)
	nombre = models.CharField(max_length=200, null=False)
	creditos = models.CharField(max_length=10, null=False)
	codigo = models.CharField(max_length=50, null=False)
	duracion = models.CharField(max_length=10, null=False)
	obligatoria = models.BooleanField(default =True)
	ciclo = models.ForeignKey(
		'Ciclo', 
		on_delete = models.CASCADE,
	)

	def __str__(self):
		return '{}'.format(self.nombre)

class PeriodoAcademico(models.Model):
	periodoAcademico_id = models.AutoField(primary_key = True)
	fechaInicio = models.DateField(auto_now = False, auto_now_add = False, null = False)
	fechaFin = models.DateField(auto_now = False, auto_now_add = False, null = False)
	estado = models.BooleanField(default =True)
	mallaCurricular = models.ForeignKey(
		'MallaCurricular', 
		on_delete = models.CASCADE,
	)
	def __str__(self):
		return '{}{}{}'.format(self.fechaInicio,"  -  ",self.fechaFin)

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

class Persona(AbstractUser):
	persona_id = models.AutoField(primary_key = True)
	cedula = models.CharField(max_length=10, unique = True, null=True)
	edad = models.CharField(max_length=3, null=True)
	fechaNacimiento =  models.DateField(auto_now = False, auto_now_add = False, null = True)
	direccion = models.TextField(max_length=200, default= 'sin direccion')
	telefono = models.CharField(max_length=13)
	foto = models.ImageField(upload_to = "gallery", null = True)
	isDecano = models.BooleanField(default = False)
	isDocente = models.BooleanField(default = False)
	isEstudiante = models.BooleanField(default = True)
	isAbogado = models.BooleanField(default = False)
	rol = models.ForeignKey(
		'Rol', 
		on_delete = models.CASCADE,
	)
	
	def __str__(self):
		return '{}{}{}'.format(self.first_name,"   ", self.last_name)

class Docente(models.Model):
	docente_id = models.AutoField(primary_key = True)
	titulo = models.CharField(max_length=200, null=False)
	persona = models.ForeignKey(
		'Persona', 
		on_delete = models.CASCADE,
	)
	carrera = models.ForeignKey(
		'Carrera', 
		on_delete = models.CASCADE,
	)

	def __str__(self):
		return '{}{}{}'.format(self.persona.first_name,"   ",self.persona.last_name)

class Silabo(models.Model):
	Silabo_id = models.AutoField(primary_key = True)
	estado = models.BooleanField(default =True)
	archivo = models.FileField(upload_to='silabos', null = False)
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

	def __str__(self):
		return '{}{}{}'.format("Silabo de: ","   ",self.materia.nombre)	

class Archivo(models.Model):
	archivo_id = models.AutoField(primary_key = True)
	archivo = models.FileField(upload_to= 'archivos', null = False)
	informePeticionario = models.FileField(upload_to='informes', null = True)
	def __str__(self):
		return '{}{}'.format("Archivo ",self.archivo_id)

class Tramite(models.Model):
	tipo =(
		('Homologacion', 'Homologacion'),
	)
	tramite_id = models.AutoField(primary_key = True)
	registro = models.CharField(max_length = 200, null = False)
	estado = models.BooleanField(default =False)
	tipo = models.CharField(max_length = 200,choices=tipo, null = False)
	carrera = models.ForeignKey(
		'Carrera',
		on_delete = models.CASCADE,
	)
	docente = models.ForeignKey(
		'Docente',
		on_delete = models.CASCADE,
	)
	archivo = models.ForeignKey(
		'Archivo', 
		on_delete = models.CASCADE,
	)
	persona = models.ForeignKey(
		'Persona', 
		on_delete = models.CASCADE,
	)

	def __str__(self):
		return '{}'.format(self.registro)

class Seguimiento(models.Model):
	seguimiento_id = models.AutoField(primary_key = True)
	revSolicitud = models.BooleanField(default =False)
	revSellos = models.BooleanField(default =False)
	asigDocente = models.BooleanField(default =False)
	revDocumentacion = models.BooleanField(default =False)
	tramite =  models.ForeignKey(
		'Tramite', 
		on_delete = models.CASCADE,
	)
	def __str__(self):
		return '{}{}'.format("Seguimiento del tramite   ", self.tramite)

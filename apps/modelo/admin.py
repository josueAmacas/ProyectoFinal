from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

class AdminPersonas(admin.ModelAdmin):
	list_display = ["persona_id","cedula","foto", "last_name", "first_name","username","email","edad","fechaNacimiento","direccion","telefono","rol","isDecano","isDocente","isAbogado","isEstudiante"]
	list_editable = ["last_name", "first_name","username","email","edad","fechaNacimiento","direccion","telefono","rol","isDecano","isDocente","isAbogado","isEstudiante"]
	list_filter = ["rol"]
	search_fields = ["cedula","last_name","rol"]
	class Meta:
		model = Persona		
admin.site.register(Persona, AdminPersonas)

class AdminRol(admin.ModelAdmin):
	list_display = ["rol_id","nombre"]
	list_editable = ["nombre"]
	class Meta:
		model = Rol
admin.site.register(Rol, AdminRol)

#admin.site.register(Persona)
admin.site.register(Carrera)
admin.site.register(MallaCurricular)
admin.site.register(Ciclo)
admin.site.register(PeriodoAcademico)
#admin.site.register(Rol)
admin.site.register(Docente)
admin.site.register(Silabo)
admin.site.register(Archivo)
admin.site.register(Tramite)
admin.site.register(Seguimiento)

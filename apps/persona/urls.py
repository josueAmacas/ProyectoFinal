from django.urls import path
from . import views

urlpatterns = [
    path('abogado', views.perfilAbogado, name= 'abogado'),
    path('decano', views.perfilDecano, name= 'decano'),
    path('docente', views.perfilDocente, name= 'docente'),
    path('solicitante', views.perfilSolicitante, name= 'solicitante'),
    path('perfilSolicitante', views.editarPerfilSolicitante),
    path('perfilDocente', views.editarPerfilDocente),
    path('perfilAbogado', views.editarPerfilAbogado),
    path('perfilDecano', views.editarPerfilDecano),
    path('requisitosDocente', views.requisitosDocente),
    path('requisitosSolicitante', views.requisitosSolicitante),
    path('requisitosDecano', views.requisitosDecano),
    path('requisitosAbogado', views.requisitosAbogado),
    path('asignacionDocentes', views.asignacionesDecano),
    path('solicitudesDecano', views.solicitudesDecano),
    path('listaUsuarios', views.listaUsuarios),
    path('listaDocentes', views.listaDocentes),
    path('planDecano', views.planDecano),
    path('planAbogado', views.planAbogado),
    path('planDocente', views.planDocente),
    path('cargarPersona', views.cargarPersona),
    path('cargarDocente', views.cargarDocente),
]
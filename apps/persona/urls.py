from django.urls import path
from . import views

urlpatterns = [
    path('solicitante', views.perfilSolicitante, name= 'solicitante'),
    path('tramiteSolicitante', views.tramiteSolicitante),
    path('seguimientoSolicitante', views.seguimientoSolicitante),
    path('mallaCurricular', views.mallaCurricular),
    path('perfilUsuario', views.editarPerfil),
    path('requisitos', views.requisitos),
    path('abogado', views.perfilAbogado, name= 'abogado'),
    path('decano', views.perfilDecano, name= 'decano'),
    path('docente', views.perfilDocente, name= 'docente'),
    
]
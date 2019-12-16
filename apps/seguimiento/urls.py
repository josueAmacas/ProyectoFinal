from django.urls import path
from . import views

urlpatterns = [
    path('seguimientoSolicitante', views.seguimientoSolicitante),
    path('seguimientoAbogado', views.seguimientoAbogado),
    path('seguimientoDocente', views.seguimientoDocente),
    path('seguimientoDecano', views.seguimientoDecano),
   
    
]
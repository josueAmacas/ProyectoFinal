from django.urls import path
from . import views

urlpatterns = [
    path('tramiteSolicitante', views.tramiteSolicitante),
    path('tramiteAbogado', views.tramiteAbogado),
    path('tramiteDecano', views.tramiteDecano),
    path('tramiteDocente', views.tramiteDocente),
    
]
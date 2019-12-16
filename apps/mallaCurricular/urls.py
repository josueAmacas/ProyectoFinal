from django.urls import path
from . import views 

urlpatterns = [
   path('mallaSolicitante', views.mallaSolicitante, name= 'mallaSolicitante'),
   path('mallaDocente', views.mallaDocente, name= 'mallaDocente'),
   path('mallaAbogado', views.mallaAbogado, name= 'mallaAbogado'),
   path('mallaDecano', views.mallaDecano, name= 'mallaDecano'),
    
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ingresar),
    path('registro/', views.registro),
    #path(r'^registro/$', views.cuentaUnica), 

]
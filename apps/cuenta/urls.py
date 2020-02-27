from django.urls import path
from . import views

urlpatterns = [
    path('', views.ingresar, name='auntenticar'),
    path('registro/', views.registro),
    #path(r'^registro/$', views.cuentaUnica), 

]
from django.urls import path
from . import views

urlpatterns = [
    path('silaboDecano', views.silaboDecano, name= 'silaboDocente'),
    path('silaboDocente', views.silaboDocente ),
]
from django.urls import path
from . import views

urlpatterns = [
    path('silaboDecano', views.silaboDecano ),
    path('silaboDocente', views.silaboDocente ),
]
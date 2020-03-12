"""ProyectoFinal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import logout_then_login
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),    
    path('', views.homePage, name='index'),
    path('accounts/login/', include('apps.cuenta.urls')),
    path('personas/', include('apps.persona.urls')),
    path('mallaCurricular/', include('apps.mallaCurricular.urls')),
    path('tramite/', include('apps.tramite.urls')),
    path('seguimiento/', include('apps.seguimiento.urls')), 
    path('periodoAcademico/', include('apps.periodoAcademico.urls')),
    path('silabo/', include('apps.silabo.urls')),
    path('logout/', logout_then_login, name = 'logout'),
]
                         
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

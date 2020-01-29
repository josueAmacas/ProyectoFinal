from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Persona

admin.site.register(Persona, UserAdmin)


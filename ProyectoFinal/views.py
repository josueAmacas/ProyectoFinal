from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.urls import reverse
from apps.cuenta.views import ingresar

def homePage(request):
	return HttpResponseRedirect(reverse(ingresar))
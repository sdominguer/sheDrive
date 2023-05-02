from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from paginaweb.forms import FormularioCreacion, FormularioInicioSesion

# Create your views here.

def Home(request):
    return render(request, "paginaweb/home.html")

def Login(request):
    formulario_login=FormularioInicioSesion()
    return render(request, "paginaweb/login.html", {"formLogin":formulario_login})
    

def Signup(request):
    formulario_signup=FormularioCreacion()
    return render(request, "paginaweb/signup.html", {"formSignup":formulario_signup})


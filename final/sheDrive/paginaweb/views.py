from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from paginaweb.forms import FormularioCreacion, FormularioInicioSesion
from paginaweb.models import Usuario

# Create your views here.

def Home(request):
    return render(request, "paginaweb/home.html")

def Perfil(request):
    return render(request, "paginaweb/perfil.html")

def Viaje(request):
    return render(request, "paginaweb/viaje.html")

def Tarjeta(request):
    return render(request, "paginaweb/tarjeta.html")

def Login(request):
    formulario_login=FormularioInicioSesion()
    return render(request, "paginaweb/login.html", {"formLogin":formulario_login})
    
def Signup(request):
    formulario_signup=FormularioCreacion()
    if request.method=="POST":
        formulario_signup=FormularioCreacion(data=request.POST)
        if formulario_signup.is_valid():
            telefono=request.POST.get("telefono")
            nombre=request.POST.get("nombre")
            identificacion=request.POST.get("identificacion")
            contraseña=request.POST.get("contraseña")
            email=request.POST.get("email")

            usuario = Usuario(telefono=telefono, nombre=nombre, identificacion=identificacion, contraseña=contraseña, email=email)
            usuario.save()

            return redirect("/signup/?valido")


    return render(request, "paginaweb/signup.html", {"formSignup":formulario_signup})




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

from django.shortcuts import render

from django.shortcuts import render

def Viaje(request):
    origin = request.GET.get('origin')
    destination = request.GET.get('destination')
    
    context = {
        'origin': origin,
        'destination': destination
    }
    
    return render(request, 'paginaweb/viaje.html', context)



def Tarjeta(request):
    return render(request, "paginaweb/tarjeta.html")

def InicioViaje(request):
    return render(request, "paginaweb/inicioViaje.html")


from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import FormularioInicioSesion

from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import FormularioInicioSesion

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect



def Login(request):
    if request.method == "POST":
        form = FormularioInicioSesion(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            contraseña = form.cleaned_data["contraseña"]

            # Validar los datos en la base de datos
            try:
                usuario = Usuario.objects.get(email=email, contraseña=contraseña)
                # Iniciar sesión al usuario
                request.session['usuario_id'] = usuario.id
                return redirect("Home")  # Redireccionar a la página de inicio de sesión exitosa
            except Usuario.DoesNotExist:
                return redirect("/login/?invalido")  # Redireccionar a la página de inicio de sesión inválido
    else:
        form = FormularioInicioSesion()

    return render(request, "paginaweb/login.html", {"form": form})


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




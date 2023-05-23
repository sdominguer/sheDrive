from django.urls import path

from paginaweb import views

urlpatterns = [
    path("", views.Home, name="Home"),
    path("signup/",views.Signup, name="Signup"),
    path("login/",views.Login, name="Login"),
    path("viaje/",views.Viaje, name="Viaje"),
    path("perfil.html", views.Perfil, name="Perfil"),
    path('tarjeta/', views.Tarjeta, name='Tarjeta'),
    path('inicioViaje/', views.InicioViaje, name='InicioViaje'),


]
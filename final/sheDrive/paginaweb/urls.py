from django.urls import path

from paginaweb import views

urlpatterns = [
    path("", views.Home, name="Home"),
    path("signup/",views.Signup, name="Signup"),
    path("login/",views.Login, name="Login"),
]
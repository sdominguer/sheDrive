from django import forms

class FormularioCreacion(forms.Form):
    nombre=forms.CharField(label="Nombre", required=True)
    identificacion=forms.CharField(label="Identificación", required=True)
    contraseña=forms.CharField(label= "Contraseña", required=True, widget=forms.PasswordInput())
    email=forms.EmailField(label="Correo", required=True)
    telefono=forms.CharField(label="Teléfono", required=True)

class FormularioInicioSesion(forms.Form):
    email=forms.EmailField(label="Correo", required=True)
    password=forms.CharField(label="Contraseña", required=True)


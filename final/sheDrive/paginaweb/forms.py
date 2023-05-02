from django import forms

class FormularioCreacion(forms.Form):
    first_name=forms.CharField(label="Nombre", required=True)
    identification=forms.CharField(label="Identificación", required=True)
    password=forms.CharField(label="Contraseña", required=True)
    email=forms.EmailField(label="Correo", required=True)
    telefono=forms.CharField(label="Telefono", required=True)

class FormularioInicioSesion(forms.Form):
    email=forms.EmailField(label="Correo", required=True)
    password=forms.CharField(label="Contraseña", required=True)
from django import forms
from .models import Usuarios

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = ['nombres', 'apellidos', 'rut', 'direccion', 'telefono_personal', 'correo_electronico', 'tipo_usuario']
        widgets = {
            'tipo_usuario': forms.Select()
        }
from django import forms
from .models import Usuarios, Inmuebles

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = ['nombres', 'apellidos', 'rut', 'direccion', 'telefono_personal', 'correo_electronico', 'tipo_usuario']
        widgets = {
            'tipo_usuario': forms.Select()
        }
        
class InmuebleForm(forms.ModelForm): 
    class Meta:
        model = Inmuebles
        fields = ['nombre', 'descripcion', 'metros_cuadrados_construidos', 'metros_cuadrados_totales_o_del_terreno', 
                  'cantidad_de_estacionamientos', 'cantidad_de_habitaciones', 'direccion', 'tipo_de_inmueble', 
                  'precio_mensual_del_arriengo', 'disponible', 'comuna']

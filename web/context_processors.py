from .models import Usuarios

def es_arrendador(request):
    if request.user.is_authenticated:
        try:
            usuario = Usuarios.objects.get(id=request.user.id)
            return {'es_arrendador': usuario.tipo_usuario.rol == 'arrendador'}
        except Usuarios.DoesNotExist:
            return {'es_arrendador': False}
    return {'es_arrendador': False}

def es_arrendatario(request):
    if request.user.is_authenticated:
        try:
            usuario = Usuarios.objects.get(id=request.user.id)  # Asegúrate de usar el ID
            return {'es_arrendatario': usuario.tipo_usuario.rol == 'arrendatario'}
        except Usuarios.DoesNotExist:
            return {'es_arrendatario': False}
    return {'es_arrendatario': False}

from .models import Usuarios

def es_arrendador(request):
    if request.user.is_authenticated:
        try:
            usuario = Usuarios.objects.get(id=request.user.id)
            return {'es_arrendador': usuario.tipo_usuario.rol == 'arrendador'}
        except Usuarios.DoesNotExist:
            return {'es_arrendador': False}
    return {'es_arrendador': False}

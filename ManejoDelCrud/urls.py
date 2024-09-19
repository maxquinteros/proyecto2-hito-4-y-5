from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from web.views import index, usuario, login, register, editar_perfil, agregar_inmueble, ver_inmuebles, editar_inmueble, eliminar_inmueble

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('usuario/', editar_perfil, name='usuario'),
    path('agregar_inmueble/', agregar_inmueble, name='agregar_inmueble'),
    path('ver_inmuebles/', ver_inmuebles, name='ver_inmuebles'),
    path('editar_inmueble/<int:inmueble_id>/', editar_inmueble, name='editar_inmueble'),
    path('eliminar_inmueble/<int:inmueble_id>/', eliminar_inmueble, name='eliminar_inmueble'),
]

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from web.models import Usuarios, Roles, Inmuebles, UsuariosInmuebles
from .forms import UsuarioForm, InmuebleForm


# Create your views here.
def index(request):
    return render(request, "index.html", {})


def usuario(request):
    return render(request, "usuario.html", {})


def login(request):
    return render(request, "login.html", {})


def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        role = request.POST.get("role")

        if password1 == password2:
            try:
                user = User.objects.create_user(username=username, password=password1)

                tipo_usuario = Roles.objects.get(rol=role)
                Usuarios.objects.create(
                    nombres=username,
                    apellidos="",
                    rut="",
                    correo_electronico=user.email,
                    tipo_usuario=tipo_usuario,
                )

                auth_login(request, user)
                return redirect("index")

            except Exception as e:
                return render(request, "register.html", {"error": str(e)})
    else:
        return render(request, "register.html")

@login_required
def editar_perfil(request):
    user = request.user
    usuario = get_object_or_404(Usuarios, id=user.id)

    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('usuario')
    else:
        form = UsuarioForm(instance=usuario)

    context = {
        'form': form,
        'es_arrendador': usuario.tipo_usuario.rol == 'arrendador'
    }

    return render(request, 'usuario.html', context)

@login_required
def agregar_inmueble(request):
    if request.method == 'POST':
        form = InmuebleForm(request.POST)
        if form.is_valid():
            inmueble = form.save(commit=False)
            try:
                # Busca el perfil del usuario basado en el correo electrónico
                usuarios = Usuarios.objects.filter(correo_electronico=request.user.email)

                if usuarios.exists():
                    usuario = usuarios.first()  # Obtén el primer usuario (ajusta según sea necesario)
                    inmueble.save()
                    UsuariosInmuebles.objects.create(
                        id_fk_usuario=usuario,
                        id_fk_inmuebles=inmueble
                    )
                    return redirect('ver_inmuebles')
                else:
                    form.add_error(None, 'No se encontró el perfil del usuario.')
            except Exception as e:
                form.add_error(None, str(e))
    else:
        form = InmuebleForm()

    return render(request, 'agregar_inmueble.html', {'form': form})


@login_required
def ver_inmuebles(request):
    if not request.user.is_authenticated:
        return redirect('login')
    usuarios = Usuarios.objects.filter(correo_electronico=request.user.email)
    if usuarios.exists():
        usuario = usuarios.first()
        inmuebles_ids = UsuariosInmuebles.objects.filter(id_fk_usuario=usuario).values_list('id_fk_inmuebles', flat=True)
        inmuebles = Inmuebles.objects.filter(id__in=inmuebles_ids)
    else:
        inmuebles = Inmuebles.objects.none()

    return render(request, 'ver_inmuebles.html', {'inmuebles': inmuebles})

@login_required
def editar_inmueble(request, inmueble_id):
    inmueble = get_object_or_404(Inmuebles, id=inmueble_id)

    if request.method == 'POST':
        form = InmuebleForm(request.POST, instance=inmueble)
        if form.is_valid():
            form.save()
            return redirect('ver_inmuebles')
    else:
        form = InmuebleForm(instance=inmueble)

    return render(request, 'editar_inmueble.html', {'form': form, 'inmueble': inmueble})

@login_required
def eliminar_inmueble(request, inmueble_id):
    inmueble = get_object_or_404(Inmuebles, id=inmueble_id)

    if request.method == 'POST':
        inmueble.delete()
        return redirect('ver_inmuebles')

    return render(request, 'confirmar_eliminacion.html', {'inmueble': inmueble})
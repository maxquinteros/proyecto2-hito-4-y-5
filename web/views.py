from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from web.models import Usuarios, Roles
from .forms import UsuarioForm


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
    
    return render(request, 'usuario.html', {'form': form})
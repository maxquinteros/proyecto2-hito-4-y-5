import os
import sys
import django
from datetime import date

# Configura el entorno de Django
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ManejoDelCrud.settings")
django.setup()

from web.models import (
    Roles,
    Inmuebles,
    Comunas,
    TipoInmueble,
    Usuarios,
    UsuariosInmuebles,
)


def crear_roles():
    rol = Roles(rol="arrendatario")
    rol.save()
    print(f"El rol {rol.rol} ha sido creado con éxito")

    rol = Roles(rol="arrendador")
    rol.save()
    print(f"El rol {rol.rol} ha sido creado con éxito")

    rol = Roles(rol="vendedor")
    rol.save()
    print(f"El rol {rol.rol} ha sido creado con éxito")


# crear_roles()


def enlistar_roles():
    roles = Roles.objects.all()
    print("Los roles existentes son:")
    for rol in roles:
        print(rol.rol)


# enlistar_roles()


def cambiar_rol():
    rol = Roles.objects.get(rol="vendedor")
    rol.rol = "comprador"
    rol.save()
    print(f"El rol {rol.rol} ha sido modificado con éxito")


# cambiar_rol()


def eliminar_rol():
    rol = Roles.objects.get(rol="comprador")
    rol.delete()
    print(f"El rol {rol.rol} ha sido eliminado con éxito")


# eliminar_rol


def consultar_inmuebles_por_comuna():
    inmuebles_por_comuna = {}

    comunas = Comunas.objects.all()

    for comuna in comunas:
        inmuebles = Inmuebles.objects.filter(comuna=comuna, disponible=True).values(
            "nombre", "descripcion"
        )

        inmuebles_por_comuna[comuna.comuna] = list(inmuebles)

    for comuna, inmuebles in inmuebles_por_comuna.items():
        print(f"Comuna: {comuna}")
        for inmueble in inmuebles:
            print(
                f" - Nombre: {inmueble['nombre']}, Descripción: {inmueble['descripcion']}"
            )

    return inmuebles_por_comuna


# consultar_inmuebles_por_comuna()


def consultar_inmuebles_por_region():
    inmuebles_por_region = {}
    comunas = Comunas.objects.all()

    for comuna in comunas:
        inmuebles = Inmuebles.objects.filter(comuna=comuna, disponible=True).values(
            "nombre", "descripcion"
        )

        if comuna.region not in inmuebles_por_region:
            inmuebles_por_region[comuna.region] = []

        inmuebles_por_region[comuna.region].extend(list(inmuebles))

    for region, inmuebles in inmuebles_por_region.items():
        print(f"Región: {region}")
        for inmueble in inmuebles:
            print(
                f" - Nombre: {inmueble['nombre']}, Descripción: {inmueble['descripcion']}"
            )

    return inmuebles_por_region


consultar_inmuebles_por_region()

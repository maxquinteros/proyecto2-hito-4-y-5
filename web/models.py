from django.db import models


# Create your models here.
class Comunas(models.Model):
    comuna = models.CharField(
        db_column="Comuna", primary_key=True
    )  # Field name made lowercase.
    region = models.CharField(db_column="Region")
    
    def __str__(self):
        return self.comuna
    
    class Meta:
        managed = False
        db_table = "comunas"


class Inmuebles(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    metros_cuadrados_construidos = models.FloatField()
    metros_cuadrados_totales_o_del_terreno = models.FloatField()
    cantidad_de_estacionamientos = models.IntegerField()
    cantidad_de_habitaciones = models.IntegerField()
    direccion = models.CharField(max_length=255)
    tipo_de_inmueble = models.ForeignKey(
        "TipoInmueble",
        models.DO_NOTHING,
        db_column="tipo_de_inmueble",
        blank=True,
        null=True,
    )
    precio_mensual_del_arriengo = models.IntegerField()
    disponible = models.BooleanField(blank=True, null=True)
    comuna = models.ForeignKey(
        Comunas, models.DO_NOTHING, db_column="comuna", blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "inmuebles"

    def __str__(self):
        return self.nombre


class Roles(models.Model):
    rol = models.CharField(unique=True, max_length=50)

    def __str__(self):
        return self.rol

    class Meta:
        managed = False
        db_table = "roles"


class TipoInmueble(models.Model):
    inmueble = models.CharField(unique=True, max_length=50)

    def __str__(self):
        return self.inmueble

    class Meta:
        managed = False
        db_table = "tipo_inmueble"


class Usuarios(models.Model):
    nombres = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    rut = models.CharField(max_length=10)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    telefono_personal = models.CharField(max_length=12, blank=True, null=True)
    correo_electronico = models.CharField(max_length=250)
    tipo_usuario = models.ForeignKey(
        Roles, models.DO_NOTHING, db_column="tipo_usuario", blank=True, null=True
    )

    def __str__(self):
        return f"{self.nombres} {self.apellidos} ({self.tipo_usuario})"

    class Meta:
        managed = False
        db_table = "usuarios"


class UsuariosInmuebles(models.Model):
    id_fk_usuario = models.ForeignKey(
        Usuarios, models.DO_NOTHING, db_column="id_fk_usuario", blank=True, null=True
    )
    id_fk_inmuebles = models.ForeignKey(
        Inmuebles, models.DO_NOTHING, db_column="id_fk_inmuebles", blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "usuarios_inmuebles"

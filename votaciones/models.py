from django.db import models

# Create your models here.



from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import F, Q
from django.utils import timezone



# 1. MODELO EDICION


class Edicion(models.Model):
    id_edicion = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150)
    anio = models.PositiveIntegerField(unique=True)

    def __str__(self):
        return f"{self.nombre} - {self.anio}"

    class Meta:
        verbose_name = "Edición"
        verbose_name_plural = "Ediciones"
        ordering = ["-anio"]



# 2. MODELO CATEGORIA


class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)

    edicion = models.ForeignKey(
        Edicion,
        on_delete=models.PROTECT,
        related_name="categorias"
    )

    nombre = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return f"{self.nombre} - {self.edicion.anio}"

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ["nombre"]

        constraints = [
            models.UniqueConstraint(
                fields=["edicion", "nombre"],
                name="categoria_unica_por_edicion"
            )
        ]



# 3. MODELO VOTACION


class Votacion(models.Model):

    class Estado(models.TextChoices):
        PENDIENTE = "pendiente", "Pendiente"
        ACTIVA = "activa", "Activa"
        CERRADA = "cerrada", "Cerrada"

    id_votacion = models.AutoField(primary_key=True)

    categoria = models.OneToOneField(
        Categoria,
        on_delete=models.PROTECT,
        related_name="votacion"
    )

    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()

    estado = models.CharField(
        max_length=20,
        choices=Estado.choices,
        default=Estado.PENDIENTE
    )

    def clean(self):
        super().clean()

        if (
            self.fecha_inicio
            and self.fecha_fin
            and self.fecha_fin <= self.fecha_inicio
        ):
            raise ValidationError({
                "fecha_fin": (
                    "La fecha de finalización debe ser "
                    "posterior a la fecha de inicio."
                )
            })

    def esta_abierta(self):
        ahora = timezone.now()

        return (
            self.estado == self.Estado.ACTIVA
            and self.fecha_inicio <= ahora < self.fecha_fin
        )

    def __str__(self):
        return f"Votación - {self.categoria}"

    class Meta:
        verbose_name = "Votación"
        verbose_name_plural = "Votaciones"

        constraints = [
            models.CheckConstraint(
                condition=Q(fecha_fin__gt=F("fecha_inicio")),
                name="fechas_validas_votacion"
            )
        ]



# 4. MODELO OPCION


class Opcion(models.Model):
    id_opcion = models.AutoField(primary_key=True)

    votacion = models.ForeignKey(
        Votacion,
        on_delete=models.PROTECT,
        related_name="opciones"
    )

    nombre_participante = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre_participante

    class Meta:
        verbose_name = "Opción"
        verbose_name_plural = "Opciones"
        ordering = ["nombre_participante"]



# 5. MODELO VOTO

class Voto(models.Model):
    id_voto = models.AutoField(primary_key=True)

    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="votos"
    )

    votacion = models.ForeignKey(
        Votacion,
        on_delete=models.PROTECT,
        related_name="votos"
    )

    opcion = models.ForeignKey(
        Opcion,
        on_delete=models.PROTECT,
        related_name="votos"
    )

    fecha_hora = models.DateTimeField(default=timezone.now)

    def clean(self):
        super().clean()

        if not self.votacion_id or not self.opcion_id:
            return

        if self.opcion.votacion_id != self.votacion_id:
            raise ValidationError(
                "La opción seleccionada no pertenece "
                "a esta votación."
            )

        if self._state.adding and not self.votacion.esta_abierta():
            raise ValidationError(
                "La votación no está abierta actualmente."
            )

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Voto {self.id_voto} - {self.usuario}"

    class Meta:
        verbose_name = "Voto"
        verbose_name_plural = "Votos"

#Lo siguiente lo implmentamos pr evitar una segunda votación en una misma categoria 
        constraints = [
            models.UniqueConstraint(
                fields=["usuario", "votacion"],
                name="voto_unico_por_usuario_votacion"
            )
        ]

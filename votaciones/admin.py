from django.contrib import admin

# Register your models here.


from .models import Edicion, Categoria, Votacion, Opcion, Voto


# Administración de ediciones
@admin.register(Edicion)
class EdicionAdmin(admin.ModelAdmin):
    list_display = ("id_edicion", "nombre", "anio")
    search_fields = ("nombre",)
    ordering = ("-anio",)


# Administración de categorías
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("id_categoria", "nombre", "edicion")
    list_filter = ("edicion",)
    search_fields = ("nombre",)


# Administración de votaciones
@admin.register(Votacion)
class VotacionAdmin(admin.ModelAdmin):
    list_display = (
        "id_votacion",
        "categoria",
        "fecha_inicio",
        "fecha_fin",
        "estado",
    )
    list_filter = ("estado",)


# Administración de opciones
@admin.register(Opcion)
class OpcionAdmin(admin.ModelAdmin):
    list_display = (
        "id_opcion",
        "nombre_participante",
        "votacion",
    )
    search_fields = ("nombre_participante",)


# Consulta de votos
@admin.register(Voto)
class VotoAdmin(admin.ModelAdmin):
    list_display = (
        "id_voto",
        "usuario",
        "votacion",
        "opcion",
        "fecha_hora",
    )

    list_filter = ("votacion",)
    readonly_fields = (
        "usuario",
        "votacion",
        "opcion",
        "fecha_hora",
    )

    # Evitar crear votos manualmente desde Admin
    def has_add_permission(self, request):
        return False

    # Evitar modificar votos desde Admin
    def has_change_permission(self, request, obj=None):
        return False

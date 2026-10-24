
from django.urls import path
from . import views

urlpatterns = [
    path(
        "",
        views.lista_votaciones,
        name="lista_votaciones"
    ),

    path(
        "categoria/<int:id_categoria>/",
        views.votacion_categoria,
        name="votacion_categoria"
    ),
]
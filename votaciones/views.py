from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import Categoria, Votacion, Opcion


def lista_votaciones(request):
    votaciones = Votacion.objects.select_related(
        "categoria",
        "categoria__edicion"
    ).all().order_by("id_votacion")

    participantes_por_votacion = {}

    for opcion in Opcion.objects.all():
        participantes_por_votacion.setdefault(
            opcion.votacion_id, []
        ).append(opcion)

    registros = []

    for votacion in votaciones:
        registros.append({
            "votacion": votacion,
            "participantes": participantes_por_votacion.get(
                votacion.pk, []
            )
        })

    return render(
        request,
        "votaciones/votaciones.html",
        {"registros": registros}
    )

@login_required
def votacion_categoria(request, id_categoria):

    categoria = get_object_or_404(
        Categoria,
        pk=id_categoria
    )

    votacion = Votacion.objects.filter(
        categoria=categoria
    ).first()

    participantes = []

    if votacion:
        participantes = Opcion.objects.filter(
            votacion=votacion
        )

    return render(
        request,
        "votaciones/votacion_categoria.html",
        {
            "categoria": categoria,
            "votacion": votacion,
            "participantes": participantes
        }
    )
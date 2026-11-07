from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import Categoria, Votacion, Opcion

# para Json
from django.http import JsonResponse

# Improtaciones para la mostra mensjaes, valdiar el voto,
# controlar los errores MYSQL y poder utlizar el formulario recien creado.

from django.contrib import messages
from django.core.exceptions import ValidationError
from django.db import IntegrityError, transaction
from django.shortcuts import redirect

from .forms import VotoForm
from .models import Voto


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

    participantes = (
        Opcion.objects.filter(votacion=votacion)
        if votacion else Opcion.objects.none()
    )

    ya_voto = False
    abierta = False
    formulario = None

    if votacion:
        abierta = votacion.esta_abierta()

        ya_voto = Voto.objects.filter(
            usuario=request.user,
            votacion=votacion
        ).exists()

        if request.method == "POST":

            if ya_voto:
                messages.error(
                    request,
                    "Ya registraste tu voto en esta categoría."
                )

            elif not abierta:
                messages.error(
                    request,
                    "Esta votación no está abierta."
                )

            else:
                formulario = VotoForm(
                    request.POST,
                    votacion=votacion
                )

                if formulario.is_valid():
                    opcion = formulario.cleaned_data["opcion"]

                    try:
                        with transaction.atomic():
                            Voto.objects.create(
                                usuario=request.user,
                                votacion=votacion,
                                opcion=opcion
                            )

                    except IntegrityError:
                        messages.error(
                            request,
                            "Ya existe un voto registrado para esta categoría."
                        )

                    except ValidationError as error:
                        messages.error(
                            request,
                            "; ".join(error.messages)
                        )

                    else:
                        messages.success(
                            request,
                            "¡Tu voto se registró correctamente!"
                        )
                        return redirect(
                            "votacion_categoria",
                            id_categoria=categoria.pk
                        )

        if formulario is None:
            formulario = VotoForm(votacion=votacion)

    return render(
        request,
        "votaciones/votacion_categoria.html",
        {
            "categoria": categoria,
            "votacion": votacion,
            "participantes": participantes,
            "formulario": formulario,
            "ya_voto": ya_voto,
            "abierta": abierta,
        }
    )

    # HISTORIAL DE VOTACIONES DEL USUARIO

@login_required
def mis_votaciones(request):

    votos = Voto.objects.filter(
        usuario=request.user
    ).select_related(
        "opcion",
        "votacion",
        "votacion__categoria",
        "votacion__categoria__edicion"
    ).order_by("-fecha_hora")

    return render(
        request,
        "votaciones/mis_votaciones.html",
        {"votos": votos}
    )

# API GET - CONSULTAR CATEGORÍAS Y PARTICIPANTES

def api_categorias(request):

    if request.method != "GET":
        return JsonResponse(
            {"error": "Método no permitido. Utiliza GET."},
            status=405
        )

    categorias = Categoria.objects.select_related(
        "edicion"
    ).prefetch_related(
        "votacion__opciones"
    ).all()

    datos = []

    for categoria in categorias:

        votacion = getattr(categoria, "votacion", None)

        participantes = []

        if votacion:
            for opcion in votacion.opciones.all():
                participantes.append({
                    "id": opcion.id_opcion,
                    "nombre": opcion.nombre_participante,
                    "descripcion": opcion.descripcion
                })

        datos.append({
            "id": categoria.id_categoria,
            "nombre": categoria.nombre,
            "descripcion": categoria.descripcion,
            "edicion": {
                "id": categoria.edicion.id_edicion,
                "nombre": categoria.edicion.nombre,
                "anio": categoria.edicion.anio
            },
            "participantes": participantes
        })

    return JsonResponse(
    {"categorias": datos},
    json_dumps_params={
        "ensure_ascii": False,
        "indent": 4
    }
)
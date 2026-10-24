from votaciones.models import Edicion, Categoria
from django.shortcuts import render, get_object_or_404, redirect



def lista_ediciones(request):
    ediciones = Edicion.objects.all().order_by("-anio")

    return render(
        request,
        "ediciones/lista_ediciones.html",
        {"ediciones": ediciones}
    )


def detalle_edicion(request, id_edicion):
    edicion = get_object_or_404(
        Edicion,
        pk=id_edicion
    )

    categorias = Categoria.objects.filter(
        edicion=edicion
    ).order_by("nombre")

    return render(
        request,
        "ediciones/detalle_edicion.html",
        {
            "edicion": edicion,
            "categorias": categorias
        }
    )


def lista_categorias(request):
    categorias = Categoria.objects.select_related(
        "edicion"
    ).order_by("-edicion__anio", "nombre")

    return render(
        request,
        "ediciones/lista_categorias.html",
        {"categorias": categorias}
    )


def realizar_inscripcion(request, id_categoria):
    categoria = get_object_or_404(Categoria, pk=id_categoria)
    
    if request.method == 'POST':
        Inscripcion.objects.create(
            categoria=categoria,
            nombre_completo=request.POST.get('nombre_completo'),
            tipo_documento=request.POST.get('tipo_documento'),
            documento=request.POST.get('documento'),
            fecha_nacimiento=request.POST.get('fecha_nacimiento'),
            lugar_nacimiento=request.POST.get('lugar_nacimiento'),
            ocupacion=request.POST.get('ocupacion'),
            direccion=request.POST.get('direccion'),
            barrio=request.POST.get('barrio'),
            municipio=request.POST.get('municipio'),
            departamento=request.POST.get('departamento'),
            telefono=request.POST.get('telefono'),
            correo=request.POST.get('correo'),
            acompanante_1_nombre=request.POST.get('acompanante_1_nombre'),
            acompanante_1_doc=request.POST.get('acompanante_1_doc'),
            acompanante_1_cel=request.POST.get('acompanante_1_cel'),
            primera_vez=True if request.POST.get('primera_vez') == 'on' else False,
            historial_participacion=request.POST.get('historial_participacion')
        )
        return redirect('lista_categorias')

    return render(request, 'ediciones/formulario_inscripcion.html', {
        'categoria': categoria
    })
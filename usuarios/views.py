from django.shortcuts import render
from votaciones.models import Edicion


# Create your views here.

from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.contrib.auth import logout

from .forms import RegistroForm


def registro(request):
    if request.user.is_authenticated:
        return redirect("inicio")

    if request.method == "POST":
        formulario = RegistroForm(request.POST)

        if formulario.is_valid():
            usuario = formulario.save()
            login(request, usuario)
            return redirect("inicio")
    else:
        formulario = RegistroForm()

    return render(
        request,
        "usuarios/registro.html",
        {"formulario": formulario}
    )




def iniciar_sesion(request):

    if request.user.is_authenticated:
        return redirect("lista_ediciones")

    if request.method == "POST":
        formulario = AuthenticationForm(
            request,
            data=request.POST
        )

        if formulario.is_valid():
            usuario = formulario.get_user()
            login(request, usuario)

            return redirect("lista_ediciones")

    else:
        formulario = AuthenticationForm()

    return render(
        request,
        "usuarios/login.html",
        {"formulario": formulario}
    )



def inicio(request):
    return render(request, "usuarios/inicio.html")


@require_POST
def cerrar_sesion(request):
    logout(request)
    return redirect("iniciar_sesion")

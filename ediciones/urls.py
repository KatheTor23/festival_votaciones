from django.urls import path
from . import views

urlpatterns = [
    path("", views.lista_ediciones, name="lista_ediciones"),
    path("categorias/", views.lista_categorias, name="lista_categorias"),
    path(
        "<int:id_edicion>/",
        views.detalle_edicion,
        name="detalle_edicion"
 
    ),
    path('inscripcion/categoria/<int:id_categoria>/', views.realizar_inscripcion, name='realizar_inscripcion'),
]
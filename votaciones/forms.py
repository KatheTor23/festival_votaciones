from django import forms
from .models import Opcion


# Toda la funcionalidad del fromulario de votación

class VotoForm(forms.Form):
    opcion = forms.ModelChoiceField(
        queryset=Opcion.objects.none(),
        label="Selecciona tu participante",
        empty_label="Selecciona una opción",
        widget=forms.Select(attrs={
            "class": "form-select"
        })
    )

    def __init__(self, *args, votacion=None, **kwargs):
        super().__init__(*args, **kwargs)

        if votacion is not None:
            self.fields["opcion"].queryset = Opcion.objects.filter(
                votacion=votacion
            )
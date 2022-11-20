from django import forms
from .models import Tareas

class FormularioTareas(forms.ModelForm):
    class Meta:
        model=Tareas
        fields=["titulo","descripcion","importante"]
        widgets={
            "titulo":forms.TextInput(attrs={"class":"form-control", "placeholder":"Escriba Un Titulo"}),
            "descripcion":forms.Textarea(attrs={"class":"form-control", "placeholder":"Escriba Una Descripcion"}),
            "importante":forms.CheckboxInput(attrs={"class":"form-check-input m-auto" }),
        }
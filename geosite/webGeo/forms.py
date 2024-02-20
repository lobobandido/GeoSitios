#creado por recomendacion chatgpt
# tu_app/forms.py

from django import forms

class OrdenServicioForm(forms.Form):
    numero_orden = forms.CharField(max_length=20, required=True)

class SitioForm(forms.Form):
    nombre_sitio = forms.CharField(max_length=255, required=True)
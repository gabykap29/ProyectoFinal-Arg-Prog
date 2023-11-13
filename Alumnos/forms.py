# En tu archivo forms.py
from django import forms

class CargarAlumnosForm(forms.Form):
    archivo_csv = forms.FileField()

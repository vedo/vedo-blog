from django import forms
from django.forms import ModelForm

from .models import Tablero, Columna, Tarjeta

class FormularioTarjeta ( forms.ModelForm ):

	class Meta:
		model = Tarjeta
		fields = ["nombre"]
from django.shortcuts import render
from django.views import generic

from .models import Tablero, Columna, Tarjeta

class IndexView ( generic.ListView ):
	template_name = 'canvan/index.html'
	context_object_name = 'tablas_canvan'

	def get_queryset ( self ):
		return Tablero.objects.order_by('-fecha_ultima_modificacion')


class DetailView ( 	generic.DetailView ):
	model = Tablero
	template_name = 'canvan/detail.html'

	def get_context_data( self, **kwargs ):
		context = super().get_context_data(**kwargs)
		
		lista_columnas = Columna.objects.filter(tablero = self.kwargs['pk'])
		listas_tarjetas = [Tarjeta.objects.filter(columna = columna) for columna in lista_columnas]
		ambas_listas = list(zip(lista_columnas, listas_tarjetas))

		context['lista_columna_tarjetas'] = ambas_listas

		return context
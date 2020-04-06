from django.shortcuts import render
from django.views import generic

from .models import Tablero, Columna, Tarjeta

class IndexView ( generic.ListView ):
	template_name = 'canvan/index.html'
	context_object_name = 'tablas_canvan'

	def get_queryset ( self ):
		return Tablero.objects.order_by('-fecha_ultima_modificacion')


class DetailView (generic.DetailView):
	model = Tablero
	template_name = 'canvan/detail.html'

	def get_context_data( self, **kwargs ):
		context = super().get_context_data(**kwargs)
		context['lista_columnas'] = Columna.objects.all()
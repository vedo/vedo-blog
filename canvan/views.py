from django.shortcuts import render, redirect
from django.views import generic
from django.http import Http404

from .models import Tablero, Columna, Tarjeta
from .forms import FormularioTarjeta

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

		formulario = FormularioTarjeta

		context['lista_columna_tarjetas'] = ambas_listas
		context['formulario'] = formulario

		return context


def detalleTablero( request, id_tablero ):

	try:
		tablero = Tablero.objects.get(pk = id_tablero)
		
		if request.method == 'POST':
			formulario = FormularioTarjeta(reques.POST)
			if formulario.is_valid():
				formulario.save()
			return redirect('detail ')

	except Tablero.DoesNotExist:
		raise Http404("El tablero no existe")

	return render(request, 'canvan/detail.html', context)

	
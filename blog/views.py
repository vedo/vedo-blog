from django.shortcuts import render
from django.views import generic

from .models import Articulo

# Create your views here.

class IndexView (generic.ListView):
	template_name = 'blog/index.html'
	context_object_name = 'ultimos_articulos'

	def get_queryset ( self ):
		return Articulo.objects.order_by('-fecha_publicacion')

class DetailView (generic.DetailView):
		model = Articulo
		template_name = 'blog/detail.html'

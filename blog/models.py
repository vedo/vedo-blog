from django.db import models
from tinymce.models import HTMLField
from PIL import Image


# Create your models here.

class Tag (models.Model):
	nombre = models.CharField(max_length = 200)

	def __str__(self):
		return self.nombre

class Articulo (models.Model):
	titulo = models.CharField(max_length = 200)
	fecha_publicacion = models.DateTimeField()
	autor = models.CharField(max_length = 200)
	imagen = models.ImageField(blank = True)
	contenido = HTMLField() #models.TextField()
	tags = models.ManyToManyField(Tag, blank = True)

	def __str__(self):
		return self.titulo

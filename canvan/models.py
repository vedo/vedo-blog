from django.db import models

# Create your models here.

class Tablero(models.Model):
	nombre = models.CharField( max_length = 200 )
	descripcion = models.TextField( max_length = 400 )

class Columna(models.Model):
	nombre = models.CharField( max_length = 200 )
	tabler = models.ForeignKey( Tablero, on_delete = models.CASCADE )

class Tarjeta(models.Model):
	nombre = models.CharField( max_length = 200 )
	descripcion = models.TextField( max_length = 400 )
	columna = models.ForeignKey( Columna, on_delete = models.CASCADE )

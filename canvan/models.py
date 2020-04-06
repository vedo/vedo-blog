from django.db import models

# Create your models here.

class Tablero(models.Model):
	nombre = models.CharField( max_length = 200 )
	descripcion = models.TextField( max_length = 400 )
	fecha_ultima_modificacion = models.DateTimeField()

	def __str__( self ):
		return self.nombre

class Columna(models.Model):
	nombre = models.CharField( max_length = 200 )
	tablero = models.ForeignKey( Tablero, on_delete = models.CASCADE )

	def __str__(self):
		return self.nombre

class Tarjeta(models.Model):
	nombre = models.CharField( max_length = 200 )
	descripcion = models.TextField( max_length = 400 )
	columna = models.ForeignKey( Columna, on_delete = models.CASCADE )

	def __str__(self):
		return self.nombre


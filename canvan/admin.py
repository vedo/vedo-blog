from django.contrib import admin

from .models import Tablero, Columna, Tarjeta

# Register your models here.
admin.site.register(Tablero)
admin.site.register(Columna)
admin.site.register(Tarjeta)
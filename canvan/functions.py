from django.http import JsonResponse
from .models import Tarjeta, Columna

def funcionPrueba( request ):
	return JsonResponse({'Result': "Hola JSON"})

def actualizarColumna( request ):
    tarjeta = Tarjeta.objects.get(pk = request.POST['id_tarjeta'])
    columna = Columna.objects.get(pk = request.POST['id_columna'])
    tarjeta.columna = columna
    tarjeta.save()
    return JsonResponse({'status':'ok'})


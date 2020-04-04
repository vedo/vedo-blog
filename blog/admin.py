from django.contrib import admin

from .models import Articulo, Tag

# Register your models here.
admin.site.register(Articulo)
admin.site.register(Tag)
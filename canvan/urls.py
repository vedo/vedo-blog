from django.urls import path

from . import views

app_name = 'canvan'

urlpatterns = [
    path('', views.index, name='index'),
]
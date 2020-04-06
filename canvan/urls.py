from django.urls import path

from . import views

app_name = 'canvan'

urlpatterns = [
	# ej: /canvan/ 
    path ( '', views.IndexView.as_view(), name='index' ),
    path ('<int:pk>/', views.DetailView.as_view(), name='detail')
]
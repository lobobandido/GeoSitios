#  revisar configuracion en chat gpt
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('buscar_por_orden_servicio/', views.buscar_por_orden_servicio, name='buscar_por_orden_servicio'),
    path('buscar_por_sitio/', views.buscar_por_sitio, name='buscar_por_sitio'),
    path('index/', views.index, name='index'),
] 

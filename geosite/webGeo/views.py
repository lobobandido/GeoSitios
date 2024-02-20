from django.shortcuts import render, get_object_or_404
from .models import OrdenServicio, Sitio
from .forms import OrdenServicioForm, SitioForm


def index(request):
    return render(request, 'index.html')

def buscar_por_orden_servicio(request):
    if request.method == 'POST':
        form = OrdenServicioForm(request.POST)
        if form.is_valid():
            numero_orden = form.cleaned_data['numero_orden']
            orden_servicio = get_object_or_404(OrdenServicio, numero=numero_orden)
            return render(request, 'webGeo/resultado_orden_servicio.html', {'orden_servicio': orden_servicio})
    else:
        form = OrdenServicioForm()

    return render(request, 'webGeo/buscar_orden_servicio.html', {'form': form})

def buscar_por_sitio(request):
    if request.method == 'POST':
        form = SitioForm(request.POST)
        if form.is_valid():
            nombre_sitio = form.cleaned_data['nombre_sitio']
            sitio = get_object_or_404(Sitio, nombre=nombre_sitio)
            return render(request, 'webGeo/resultado_sitio.html', {'sitio': sitio})
    else:
        form = SitioForm()

    return render(request, 'twebGeo/buscar_sitio.html', {'form': form})


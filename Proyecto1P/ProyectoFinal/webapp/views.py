from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from empleados.models import Empleado


# Create your views here.

def mostrar_empleados(request):
    cantidad_empleados = Empleado.objects.count()
    pagina = loader.get_template('empleados.html')
    empleados = Empleado.objects.order_by('apellido', 'nombre')
    datos = {'cantidad': cantidad_empleados, 'empleados': empleados}

    return HttpResponse(pagina.render(datos, request))
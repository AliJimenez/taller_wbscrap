from django.shortcuts import render, get_object_or_404
from django.forms import modelform_factory
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from empleados.forms import EmpleadoFormulario
from empleados.models import Empleado

# Create your views here.
def agregar_empleado(request):
    pagina = loader.get_template('agregar_empleado.html')
    if request.method == 'GET':
        formulario = EmpleadoFormulario
    elif request.method == 'POST':
        formulario = EmpleadoFormulario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('inicio')
    datos = {'formulario': formulario}
    return HttpResponse(pagina.render(datos, request))

def ver_empleado(request, idEmpleado):
    pagina = loader.get_template('ver_empleado.html')
    empleado = get_object_or_404(Empleado, pk=idEmpleado)
    mensaje = {'empleado': empleado}
    return HttpResponse(pagina.render(mensaje, request))

def editar_empleado(request, idEmpleado):
    pagina = loader.get_template('editar_empleado.html')
    empleado = get_object_or_404(Empleado, pk=idEmpleado)
    if request.method == 'GET':
        formulario = EmpleadoFormulario(instance=empleado)
    elif request.method == 'POST':
        formulario = EmpleadoFormulario(request.POST, instance=empleado)
        if formulario.is_valid():
            formulario.save()
            return redirect('inicio')
    mensaje = {'formulario': formulario}
    return HttpResponse(pagina.render(mensaje, request))

def eliminar_empleado(request, idEmpleado):
    empleado = get_object_or_404(Empleado, pk=idEmpleado)
    if empleado:
        empleado.delete()
        return redirect('inicio')


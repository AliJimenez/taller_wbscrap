from django.shortcuts import render, get_object_or_404
from django.forms import modelform_factory
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from Personas.forms import PersonaFormulario
from Personas.models import Persona

#PersonaFormulario = modelform_factory(Persona, exclude=[])
# Create your views here.
def agregar_persona(request):
    pagina = loader.get_template('agregar_personas.html')
    if request.method == 'GET':
        formulario = PersonaFormulario
    elif request.method == 'POST':
        formulario = PersonaFormulario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('inicio')
    datos = {'formulario': formulario}
    return HttpResponse(pagina.render(datos, request))


def ver_persona(request, idPersona):
    pagina = loader.get_template('ver_persona.html')
    #persona = Persona.object.get(pk=idPersona)
    persona = get_object_or_404(Persona, pk=idPersona)
    mensaje = {'persona': persona}
    return HttpResponse(pagina.render(mensaje, request))

def editar_persona(request, idPersona):
    pagina = loader.get_template('editar_persona.html')
    persona = get_object_or_404(Persona, pk=idPersona)
    if request.method == 'GET':
        formulario = PersonaFormulario(instance=persona)
    elif request.method == 'POST':
        formulario = PersonaFormulario(request.POST, instance=persona)
        if formulario.is_valid():
            formulario.save()
            return redirect('inicio')
    mensaje = {'formulario': formulario}
    return HttpResponse(pagina.render(mensaje, request))

def eliminar_persona(request, idPersona):
    persona = get_object_or_404(Persona, pk=idPersona)
    if persona:
        persona.delete()
        return redirect('inicio')
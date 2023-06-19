from django.forms import ModelForm, EmailInput

from Personas.models import Persona


class PersonaFormulario(ModelForm):
    class Meta:
        model = Persona
        fields = ('nombre', 'apellido','sexo', 'email','activo', 'titulo', 'curso')
        widgets = {
            'email': EmailInput(attrs={'type': 'email'})
        }

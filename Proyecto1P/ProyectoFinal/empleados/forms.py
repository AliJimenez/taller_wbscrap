from django.forms import ModelForm, EmailInput

from empleados.models import Empleado


class EmpleadoFormulario(ModelForm):
    class Meta:
        model = Empleado
        fields = ('nombre', 'apellido', 'sexo', 'email', 'direccion', 'sueldo', 'departamento', 'proyecto', 'jornada')
        widgets = {
            'email': EmailInput(attrs={'type': 'email'})
        }

from django.contrib import admin
from .models import Empleado, Departamento, Proyecto, Jornada

admin.site.register(Empleado)
admin.site.register(Departamento)
admin.site.register(Proyecto)
admin.site.register(Jornada)
# Register your models here.

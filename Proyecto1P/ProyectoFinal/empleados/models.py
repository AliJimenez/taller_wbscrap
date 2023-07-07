from django.db import models


class Departamento(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=50)
    jefe = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nombre}'

class Proyecto(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=200)
    fecha_inicio = models.DateField(null=True)
    fecha_fin = models.DateField(null=True)
    cliente = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nombre}'

class Jornada(models.Model):
    TIPO = [
        ("M", "Matutino"),
        ("V", "Vespertino"),
        ("N", "Nocturno"),
    ]

    codigo = models.CharField(max_length=10)
    tipo = models.CharField(max_length=1, choices=TIPO, null=True)

    def __str__(self):
        return f'{self.tipo}'

# Create your models here.
class Empleado(models.Model):
    SEXO = [
        ("M", "Masculino"),
        ("F", "Femenino"),
    ]

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    sexo = models.CharField(max_length=1, choices=SEXO, null=True)
    email = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    sueldo = models.IntegerField(null=True)
    departamento = models.ForeignKey(Departamento, on_delete=models.SET_NULL, null=True)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.SET_NULL, null=True)
    jornada = models.ForeignKey(Jornada, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'id: {self.id} - {self.nombre} {self.apellido}'



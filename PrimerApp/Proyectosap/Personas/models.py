from django.db import models

class Curso(models.Model):
    nombre = models.CharField(max_length=20, null=True)
    horas = models.IntegerField(null=True)
    profesor = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f'{self.nombre}'



# Create your models here.
class Persona(models.Model):
    SEXO = [
        ("M", "Masculino"),
        ("F", "Femenino"),
    ]

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    sexo = models.CharField(max_length=1, choices=SEXO, null=True)
    email = models.CharField(max_length=50)
    activo = models.BooleanField(default=True)
    titulo = models.CharField(null=True, max_length=50)
    curso = models.ForeignKey(Curso, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'id: {self.id} - {self.nombre} {self.apellido}'
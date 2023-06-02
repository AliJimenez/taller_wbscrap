from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f'id: {self.id} - {self.nombre} {self.apellido}'
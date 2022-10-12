from django.db import models

# Create your models here.
class Comentario(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(max_length=150)
    departamento = models.CharField(max_length=100)
    mensaje = models.CharField(max_length=300)

    def __str__(self):
        return f"Nombre: {self.nombre} | Departamento: {self.departamento}"
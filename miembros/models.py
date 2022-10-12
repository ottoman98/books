from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Profile(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    descripcion = models.TextField(max_length=100)
    profile_pic = models.ImageField(
        null=True, default="static\images\default_images\default-avatar.png", blank=True, upload_to="images/profile/")
    departamento = models.CharField(max_length=50, default=None)
    direccion = models.CharField(max_length=50, default=None)

    # informacion de contacto
    telefono = models.CharField(max_length=10, default=None)
    whatsapp = models.CharField(max_length=10, default=None)
    facebook = models.URLField(
        ("Facebook"),
        max_length=700,
        db_index=True,
        unique=True,
        blank=True, default=None
    )

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('index')

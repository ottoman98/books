from pyexpat import model
from django.forms import ModelForm
from django import forms
from .models import Comentario


class ComentarioForm(forms.Form, ModelForm):
    nombre = forms.CharField(max_length=100, label='Nombre:', widget=forms.TextInput(attrs={'id': 'nombre' ,'placeholder': '', 'class': 'input-control'}), )

    correo = forms.EmailField(max_length=150, label='Correo:', widget=forms.EmailInput(attrs={'id': 'correo','placeholder': '', 'class': 'input-control'}), )

    departamento = forms.CharField(max_length=100, label='Departamento:', widget=forms.TextInput(attrs={'id': 'departamento', 'placeholder': '', 'class': 'input-control'}), )

    mensaje = forms.CharField(max_length=300, label='Mensaje:', widget=forms.Textarea(attrs={'id': 'mensaje', 'placeholder': '', 'class': 'input-control'}), )

    class Meta:
        model = Comentario
        fields = ['nombre', 'correo', 'departamento', 'mensaje']
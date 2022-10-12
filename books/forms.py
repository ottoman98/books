from logging import PlaceHolder
from django import forms
from .models import Books, Categorias


categorias = Categorias.objects.all().values_list('categoria', 'categoria')
categorias_list = []

for categoria in categorias:
    categorias_list.append(categoria)


estados = [('Excelente', 'Excelente'),
           ('Bueno', 'Bueno'), ('Regular', 'Regular')]
estados_list = []

for estado in estados:
    estados_list.append(estado)

intencion = [('Vender', 'Vender'), ('Regalar', 'Regalar'),
             ('Intercambiar', 'Intercambiar')]
intencion_list = []

for inten in intencion:
    intencion_list.append(inten)


class AddBookform(forms.ModelForm):
    model = Books

    titulo = forms.CharField(max_length=200, required=True, label='',  widget=forms.TextInput(
        attrs={'placeholder': 'Titulo', 'class': 'form-input'}),)

    editorial = forms.CharField(max_length=50, label='',  widget=forms.TextInput(
        attrs={'placeholder': 'Editorial', 'class': 'form-input'}),)

    categoria = forms.ChoiceField(choices=categorias_list, label='', widget=forms.Select(
        attrs={'class': 'form-input'}))

    cantidad = forms.IntegerField(
        label='', widget=forms.NumberInput(attrs={'placeholder': 'Cantidad', 'class': 'form-input'}),)

    intencion = forms.ChoiceField(choices=intencion_list, label='', widget=forms.Select(
        attrs={'class': 'form-input', 'class': 'form-input'
               }),)

    estado = forms.ChoiceField(choices=estados_list, label='', widget=forms.Select(
        attrs={'class': 'form-input', 'class': 'form-input'
               }),)

    precio = forms.IntegerField(
        label='', widget=forms.NumberInput(attrs={'placeholder': 'Precio', 'class': 'form-input'}),)

    autor = forms.CharField(max_length=200, label='', widget=forms.TextInput(
        attrs={'placeholder': 'Autor', 'class': 'form-input'}), )
    libro_img = forms.ImageField(required=True, label='Portada del libro', widget=forms.FileInput(
        attrs={'accept': ".png, .gif, .jpeg, .jpg", 'id': 'portada-input'}))

    reseña = forms.CharField(label='', max_length=2000, widget=forms.Textarea(
        attrs={'placeholder': 'Resumen o reseña corta...', 'class': 'form-input', 'style': 'resize:none;'}), )

    class Meta:
        model = Books
        fields = ('titulo', 'editorial', 'categoria', 'cantidad',
                  'intencion', 'estado', 'precio', 'autor', 'reseña', 'libro_img')

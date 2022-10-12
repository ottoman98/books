
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile


class SignUpForm(UserCreationForm):

    username = forms.CharField(max_length=100, label='Nombre de usuario:', widget=forms.TextInput(
        attrs={'placeholder': 'Nombre de usuario', 'class': 'input-control'}), )

    email = forms.EmailField(label='Correo electrónico:', widget=forms.EmailInput(
        attrs={'placeholder': 'Correo electronico', 'class': 'input-control'}))

    first_name = forms.CharField(max_length=100, label='Nombre:', widget=forms.TextInput(
        attrs={'placeholder': 'Nombre', 'class': 'input-control'}))

    last_name = forms.CharField(max_length=100, label='Apellido:', widget=forms.TextInput(
        attrs={'placeholder': 'Apellido', 'class': 'input-control'}))

    password1 = forms.CharField(max_length=100, label='Contraseña:', widget=forms.PasswordInput(
        attrs={'placeholder': 'Contraseña', 'class': 'input-control'}))

    password2 = forms.CharField(max_length=100, label='Repetir contraseña:', widget=forms.PasswordInput(
        attrs={'placeholder': 'Repetir contraseña', 'class': 'input-control'}))

    class Meta():
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1')


class UserEditForm(UserChangeForm):
    username = forms.CharField(max_length=100, label='Usuario', widget=forms.TextInput(
        attrs={'placeholder': 'Usuario', 'class': 'box', 'readonly': True}), )
    first_name = forms.CharField(max_length=100, label='Nombre', widget=forms.TextInput(
        attrs={'placeholder': 'Nombre', 'class': 'box'}), )
    last_name = forms.CharField(max_length=100, label='Apellidos', widget=forms.TextInput(
        attrs={'placeholder': 'Apellidos', 'class': 'box'}), )
    email = forms.EmailField(label='Email', widget=forms.EmailInput(
        attrs={'placeholder': 'Correo', 'class': 'box'}))

    class Meta():
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password')


class ProfileForm(forms.ModelForm):
    descripcion = forms.CharField(
        max_length=100, label='Descripción', widget=forms.Textarea())
    profile_pic = forms.ImageField(
        label='Foto de perfil', widget=forms.FileInput())
    departamento = forms.CharField(
        max_length=50, label='Departamento', widget=forms.TextInput())
    direccion = forms.CharField(
        max_length=50, label='Dirección', widget=forms.TextInput())
    telefono = forms.CharField(
        max_length=10, label='Teléfono', widget=forms.TextInput())
    whatsapp = forms.CharField(
        max_length=10, label='WhatsApp', widget=forms.TextInput())
    facebook = forms.CharField(
        max_length=600, label='Facebook', widget=forms.URLInput())

    class Meta:
        model = Profile
        fields = ('descripcion', 'profile_pic', 'departamento',
                  'direccion', 'whatsapp', 'facebook', 'telefono')


class ProfileDataForm(UserChangeForm):
    username = forms.CharField(max_length=100, label='Usuario', widget=forms.TextInput(
        attrs={'placeholder': 'Usuario', 'class': 'box', 'readonly': True}), )
    first_name = forms.CharField(max_length=100, label='Nombre', widget=forms.TextInput(
        attrs={'placeholder': 'Nombre', 'class': 'box'}), )
    last_name = forms.CharField(max_length=100, label='Apellidos', widget=forms.TextInput(
        attrs={'placeholder': 'Apellidos', 'class': 'box'}), )
    email = forms.EmailField(label='Email', widget=forms.EmailInput(
        attrs={'placeholder': 'Correo', 'class': 'box'}))

    class Meta:
        model = User
        fields = '__all__'

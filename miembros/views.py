
from multiprocessing.dummy import Manager
from django.shortcuts import render
from django.views.generic import UpdateView, CreateView
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.urls import reverse_lazy
from .forms import SignUpForm, UserEditForm, ProfileForm, ProfileDataForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.models import User
from books.models import Books
from .models import Profile

# Create your views here.


class SignUpView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')


class UserEditView(generic.UpdateView):
    form_class = UserEditForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('index')

    def get_object(self):
        return self.request.user


class PasswordChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('index')
    template_name = 'registration/changepassword.html'


def ProfileView(request):
    user = request.user
    return render(request, 'profile.html', {'user': user})


def LibrosSubidosView(request):
    user = request.user
    user_books = Books.objects.filter(usuario_id=user.pk)

    return render(request, 'libros_subidos.html', {'user': user, 'books': user_books})


def LibrosFavoritosView(request):
    user = request.user
    user_book = Books.objects.filter(likes__pk=user.pk)

    return render(request, 'libros_favoritos.html', {'user': user, 'books': user_book})


class DatosProfileView(CreateView):
    form_class = ProfileForm
    model = Profile
    template_name = 'profile_data.html'

    def form_valid(self, form):
        form.instance.user_id = self.request.user.pk
        return super().form_valid(form)


def SearchView(request):

    return render(request, 'search.html', {})


def Contact(request, pk):

    user_contact = User.objects.get(id=pk)
    user_profile = Profile.objects.get(user_id=pk)

    return render(request, 'contact.html', {'contact': user_contact, 'contact2': user_profile})


class UpdateProfileView(UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'update_profile.html'



from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .models import Books, Categorias
from .forms import AddBookform
from django.http import HttpResponseRedirect
from miembros.models import User


class IndexView(ListView):
    model = Books
    template_name = 'index.html'
    ordering = ['-fecha']

    def get_context_data(self, *args, **kwargs):

        categories_menu = Categorias.objects.all()
        context = super(IndexView, self).get_context_data(*args, **kwargs)

        context['categories_menu'] = categories_menu

        return context


class BookdetailsView(DetailView):

    model = Books
    template_name = 'book_details.html'

    def get_context_data(self, *args, **kwargs):

        context = super(BookdetailsView, self).get_context_data(
            *args, **kwargs)

        stuff = get_object_or_404(Books, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()

        liked = False
        if stuff.likes.filter(id=self.request.user.pk).exists():
            liked = True

        context['total_likes'] = total_likes
        context['liked'] = liked

        return context


class Add_BookView(CreateView):
    form_class = AddBookform

    model = Books
    template_name = 'add_book.html'

    def form_valid(self, form):
        form.instance.usuario_id = self.request.user.pk
        return super().form_valid(form)


class Update_bookView(UpdateView):
    form_class = AddBookform
    model = Books
    template_name = 'update_book.html'


class DeleteBookView(DeleteView):
    model = Books
    template_name = 'delete_book.html'
    success_url = reverse_lazy('index')


def CategoryView(request, cat):
    categories_menu = Categorias.objects.all()

    category_books = Books.objects.filter(categoria=cat.replace('-', " "))
    return render(request, 'categories.html', {'cat': cat,
                                               'category_books': category_books,
                                               'categories_aside': categories_menu})


def Likeview(request, pk):
    book = get_object_or_404(Books, id=request.POST.get('book_id'))

    liked = False

    if book.likes.filter(id=request.user.pk).exists():
        book.likes.remove(request.user)
        liked = False
    else:
        book.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('book_details', args=[str(pk)]))


def SearchView(request):

    if request.method == 'POST':
        searched = request.POST['searched']
        result = Books.objects.filter(titulo__icontains=searched)
        result_longitud = len(result) >= 1
        

        return render(request, 'search.html', {'searched': searched, 'results': result, 'result_longitud': result_longitud})
    else:
        return render(request, 'search.html', {})

from django.shortcuts import render, redirect
from .forms import ComentarioForm
from django.http import HttpResponse
# Create your views here.

def feedback(request, nombre):
    return render(request, 'feedback.html', {'nombre': nombre})

def Contactanos(request):
    # return HttpResponse('Hola mundo')
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            nombre = request.POST['nombre']
            form.save()
            return feedback(request, nombre)
            # return redirect('feedback')
    else:
        form = ComentarioForm()
        return render(request, 'contactanos.html', {'form': form})
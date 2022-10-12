from django.shortcuts import render


def about(request):
    return render(request, 'about.html', {})

def politicas(request):
    return render(request, 'politicas.html', {})

def tratamientoDatos(request):
    return render(request, 'tratamientoDatos.html', {})

def guiaUser(request):
    return render(request, 'guiaUser.html', {})

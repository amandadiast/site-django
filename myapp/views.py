from django.shortcuts import render

# Create your views here.

def paginaInicial(request):
    return render(request, "myapp/index.html")

def about(request):
    return render(request, "myapp/about.html")

def contact(request):
    return render(request, "myapp/contato.html")


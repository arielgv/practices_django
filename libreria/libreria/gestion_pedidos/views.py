from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def formulario(request):
    return render(request,"formulario.html")

def buscar(request):
    message = "El Articulo buscado es %r" %request.GET["prd"]
    return HttpResponse(message)
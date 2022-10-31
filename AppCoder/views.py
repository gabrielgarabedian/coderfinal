from django.shortcuts import render
from django.http import HttpResponse

def saludo(request): #consulta o peticion
    return HttpResponse("Hola este Es MI PRIMER APP")
                # respuesta
                
def saludo_dos(request):
    return HttpResponse("HOLA y adios")

def saludar(request,nombre):
    return HttpResponse(f"hola como estas hoy {nombre}")

def mostrar_mi_template(request): #muestra el template con render
    return render(request,"AppCoder/index.html")
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from ejemplo.models import Familiar

#clase 22 clases model - formularios rapido
class FamiliarList(ListView):
    model =Familiar

class FamiliarCrear(CreateView):
   model = Familiar
   success_url = "/panel-familia"
   fields = ["nombre", "direccion", "numero_pasaporte"]
  
class FamiliarBorrar(DeleteView):
  model = Familiar
  success_url = "/panel-familia"
    
class FamiliarActualizar(UpdateView):
  model = Familiar
  success_url = reverse_lazy("family")
  fields = ["nombre", "direccion", "numero_pasaporte"]

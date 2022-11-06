from django.shortcuts import render
from django.urls import reverse_lazy
from rutina.models import Rutina

class ListRutina(ListView):
    model= Rutina
    
class CreateRutina(ListView):
    model= Rutina
    fields= ['nombre_rutina', 'short_content', 'content','image_rutina']
    success_url = reverse_lazy(******)
    


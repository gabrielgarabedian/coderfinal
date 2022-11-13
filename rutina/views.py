from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from django.views.generic import ListView , CreateView, DeleteView, UpdateView, DetailView
from django.shortcuts import render
from django.urls import reverse_lazy
from rutina.models import Rutina, Configuracion

#def index(request):

    #return render(request, 'rutina/index.html')

@login_required
def index(request):
    configuracion = Configuracion.objects.first()
    return render(request, 'rutina/index.html',{'configuracion':configuracion})

    
class RutinaLogin(LoginView):
    template_name = 'rutina/rutina_login.html'
    next_page = reverse_lazy("lista-de-rutina")

class RutinaLogout(LogoutView):
    template_name = 'rutina/rutina_logout.html'
    
#class ProfileUpdate(UpdateView):
    #model = User
    #fields = ['username']
    #success_url = reverse_lazy("rutina-login")

class ListRutina(LoginRequiredMixin,ListView):
   model= Rutina
    
class CreateRutina(CreateView):
    model= Rutina
    fields= ['nombre_rutina', 'short_content', 'content','image_rutina']
    success_url = reverse_lazy("lista-de-rutina")
    
class SearchRutinaByName(ListView):
    def get_queryset(self):
        rutina_nombre_rutina = self.request.GET.get('rutina_nombre_rutina')
        return Rutina.objects.filter(nombre_rutina__icontains=rutina_nombre_rutina)
    
class DetailRutina(DetailView):
    model=Rutina

class DeleteRutina(DeleteView):
    model=Rutina
    success_url = reverse_lazy("lista-de-rutina")

class UpdateRutina(UpdateView):
    model=Rutina
    fields=['nombre_rutina', 'short_content', 'content']
    success_url = reverse_lazy("lista-de-rutina")

def horarios(request):
    return render(request, 'rutina/horarios.html')

def nosotros(request):
    return render(request, 'rutina/nosotros.html')

def rutinas_post(request):
    rutinas = Rutina.objects.all()
    rutinas = Rutina.objects.order_by('-date_published').all()

    return render(request, 'rutina/rutinas_post.html', {"rutina": rutinas})





    
    


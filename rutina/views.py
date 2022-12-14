from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from django.views.generic import ListView , CreateView, DeleteView, UpdateView, DetailView
from django.shortcuts import render
from django.urls import reverse_lazy
from rutina.models import Rutina, Configuracion, Grilla,Staff
from django.contrib.auth.admin import User

#def index(request):

    #return render(request, 'rutina/index.html')


def index(request):
    configuracion = Configuracion.objects.first()
    return render(request, 'rutina/index.html',{'configuracion':configuracion})

   
class RutinaLogin(LoginView):
    template_name = 'rutina/rutina_login.html'
    next_page = reverse_lazy("lista-de-rutina")

class RutinaLogout(LogoutView):
    template_name = 'rutina/rutina_logout.html'
    next_page = reverse_lazy("index-rutina")
    
class RutinaSignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("rutina-login")
    template_name = "registration/signup.html"
    
class RutinaProfileUpdate(LoginRequiredMixin,UpdateView):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email']
    success_url = reverse_lazy("rutinas-post")

class ListRutina(LoginRequiredMixin,ListView):
   model= Rutina
   paginate_by = 2
    
class CreateRutina(LoginRequiredMixin,CreateView):
    model= Rutina
    fields= ['nombre_rutina', 'short_content', 'content','image_rutina']
    success_url = reverse_lazy("lista-de-rutina")


class SearchRutinaByName(ListView):
    def get_queryset(self):
        rutina_nombre_rutina = self.request.GET.get('rutina_nombre_rutina')
        return Rutina.objects.filter(nombre_rutina__icontains=rutina_nombre_rutina)
    
class DetailRutina(DetailView):
    model=Rutina

class DeleteRutina(LoginRequiredMixin,DeleteView):
    model=Rutina
    success_url = reverse_lazy("lista-de-rutina")

class UpdateRutina(LoginRequiredMixin,UpdateView):
    model=Rutina
    fields=['nombre_rutina', 'short_content', 'content','image_rutina']
    success_url = reverse_lazy("lista-de-rutina")

def horarios(request):
    grilla = Grilla.objects.first()
    return render(request, 'rutina/horarios.html',{'grilla':grilla})

def nosotros(request):
    return render(request, 'rutina/nosotros.html')

def rutinas_post(request):
    rutinas = Rutina.objects.all()
    rutinas = Rutina.objects.order_by('-date_published').all()

    return render(request, 'rutina/rutinas_post.html', {"rutina": rutinas})

def staff(request):
    staff = Staff.objects.first()
    return render(request, 'rutina/staff_conf.html',{'staff':staff})



    
    


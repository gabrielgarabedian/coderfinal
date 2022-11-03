from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.admin import User
from django.shortcuts import render
from django.urls import reverse_lazy
from blog.models import Configuracion
from django.views import View
from django.views.generic import ListView , CreateView, DeleteView, UpdateView, DetailView
from blog.models import Post

@login_required
def index(request):
    configuracion = Configuracion.objects.first()
    return render(request, 'blog/index.html',{'configuracion':configuracion})

class SearchPostByName(ListView):
    def get_queryset(self):
        post_title = self.request.GET.get('post-title')
        return Post.objects.filter(title__icontains=post_title)
    
class ListPost(LoginRequiredMixin,ListView):
    model=Post
    
class BlogLogin(LoginView):
    template_name = 'blog/blog_login.html'
    next_page = reverse_lazy("list-post")

class BlogLogout(LogoutView):
    template_name = 'blog/blog_logout.html'

#clase23 arriba
class CreatePost(CreateView):
    model=Post
    fields = ['title', 'short_content', 'content','image']
    success_url = reverse_lazy("list-post")

class DetailPost(DetailView):
    model=Post

class UpdatePost(UpdateView):
    model=Post
    fields=['title', 'short_content', 'content','image']
    success_url = reverse_lazy("list-post")

class DeletePost(DeleteView):
    model=Post
    success_url = reverse_lazy("list-post")

class BlogSignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("blog-login")
    template_name = "registration/signup.html"

class ProfileUpdate(UpdateView):
    model = User
    fields = ['username']
    success_url = reverse_lazy("blog-login")
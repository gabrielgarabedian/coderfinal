from django.urls import path
from rutina.views import *

urlpatterns = [
     path('', index, name="index-rutina"),
     path('login/', RutinaLogin.as_view(), name="rutina-login"),
     path('logout/', RutinaLogout.as_view(), name="rutina-logout"),
     path('lista-rutina/', ListRutina.as_view(), name="lista-de-rutina"),
     path('crear-rutina/', CreateRutina.as_view(),name="crear-rutina"),
     path('delete-rutina/<int:pk>/', DeleteRutina.as_view(), name= "delete-rutina"),
     path('detail-rutina/<int:pk>/', DetailRutina.as_view(), name= "detail-rutina"),
     path('update-rutina/<int:pk>/', UpdateRutina.as_view(), name="update-rutina"),
     path('horarios/', horarios, name="horarios"),
     path('nosotros/', nosotros, name="nosotros"),
     path('rutinas-post/', rutinas_post, name="rutinas-post"),
     path('search-by-name/', SearchRutinaByName.as_view(), name="search-by-name-rutina"),

    
 
     
     ]
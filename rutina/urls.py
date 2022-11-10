from django.urls import path
from rutina.views import *


urlpatterns = [
     path('', index, name="index-rutina"),
     path('login/', RutinaLogin.as_view(), name="rutina-login"),
     path('logout/', RutinaLogout.as_view(), name="rutina-logout"),
     ]
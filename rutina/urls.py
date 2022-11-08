from django.urls import path
from rutina.views import *

urlpatterns = [
     path('', index, name="index-rutina"),

     ]
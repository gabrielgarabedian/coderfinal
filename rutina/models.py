from django.db import models

class Configuracion(models.Model):
    nombre_de_pagina=models.CharField(max_length=25)
    nombre_del_lugar=models.CharField(max_length=50)
    Boton_menu_1=models.CharField(max_length=15)
    Boton_menu_2=models.CharField(max_length=15)
    Boton_menu_3=models.CharField(max_length=15)
    Boton_menu_4=models.CharField(max_length=15)
    Boton_menu_5=models.CharField(max_length=15)
    Boton_menu_6=models.CharField(max_length=15)
    titulo_cabecera=models.CharField(max_length=70, default='')
    construido=models.CharField(max_length=70)

class Rutina(models.Model):
    nombre_rutina= models.CharField(max_length=50)
    short_content= models.CharField(max_length=70)
    content= models.TextField(max_length=5000)
    image_rutina = models.ImageField(upload_to="post", null=True, blank=True)
    date_published= models.DateTimeField(auto_now_add=True)
    
    def __str__ (self):
        return f"Numero de Rutina: {self.id} - Rutina: {self.nombre_rutina}"
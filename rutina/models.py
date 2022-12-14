from django.db import models


class Configuracion(models.Model):
    titulo_cabecera=models.CharField(max_length=70, default='')
    construido=models.CharField(max_length=70)
    titulo_secundario=models.CharField(max_length=50)
    

class Rutina(models.Model):
    nombre_rutina= models.CharField(max_length=50)
    short_content= models.CharField(max_length=70)
    content= models.TextField(max_length=5000)
    image_rutina = models.ImageField(upload_to="rutinas", null=True, blank=True)
    date_published= models.DateTimeField(auto_now_add=True)


    
    def __str__ (self):
        return f"Numero de Rutina: {self.id} - Rutina: {self.nombre_rutina}"
    
class Alimentacion(models.Model):#creada para un futuro
    title= models.CharField(max_length=50)
    creador=models.CharField(max_length=70)
    contenido= models.TextField(max_length=5000)
    image_rutina = models.ImageField(upload_to="post", null=True, blank=True)
    date_published= models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Receta: {self.id} - Alimentacion: {self.title} "
    
class Grilla(models.Model):
    dias_de=models.CharField(max_length=50, default="Lunes a Sabados")
    horario_de=models.CharField(max_length=40, default="de 8 a 22hs")
    feriados_de=models.CharField(max_length=50, default="9 a 20hs")
    
class Staff(models.Model):
    nombre_staff= models.CharField(max_length=50,default='')
    profe_de= models.CharField(max_length=50,default='')
    
    



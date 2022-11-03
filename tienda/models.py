from django.db import models

class Configuracion(models.Model):
    nombre_tienda= models.CharField(max_length=30)
    construido= models.CharField(max_length=70)
    titulo_principal= models.CharField(max_length=70, default='')
    
class Post(models.Model):
    title = models.CharField(max_length=100)
    short_content = models.CharField(max_length=100)
    content =models.TextField(max_length=5000)
    date_published= models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="post", null=True, blank=True)
    
    def __str__(self):
        return f"id:{self.id} - Title:{self.title}"
    
class Clientes(models.Model):
    nombre_cliente= models.CharField(max_length=70)
    domicilio= models.CharField(max_length=70)
    documento= models.CharField(max_length=70)
    mail= models.EmailField(max_length=200)
    
    def __str__(self):
        return f"Socio: {self.id} - Nombre: {self.nombre_cliente}"
    
class Empleado(models.Model):
    nombre_completo = models.CharField(max_length=70)
    domicilio =models.CharField(max_length=70)
    dni= models.CharField(max_length=70)
    cargo = models.CharField(max_length=70)
    sucursal = models.CharField(max_length=70)
    fecha_nacimiento= models.DateField(max_length=10)
    
    def __str__(self):
        return f" Id empleado: {self.id} - Nombre: {self.nombre_completo} - Cargo: {self.cargo} - Suc.: {self.sucursal}"

class Producto(models.Model):
    articulo = models.CharField(max_length=20)
    producto = models.CharField(max_length=100)
    art_fab = models.CharField(max_length=20)
    id_fab = models.CharField(max_length=5)
    costo = models.CharField(max_length=20)
    pvp= models.CharField(max_length=20)
    date_published= models.DateTimeField(auto_now_add=True)
    
    def __stre__(self):
        return f"Articulo:{self.articulo} - id.Fabricante:{self.id_fab} - P.v.P.:{self.pvp}"
    

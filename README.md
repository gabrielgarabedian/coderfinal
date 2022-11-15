# Proyecto Final - GYM carrey
## Integrantes:

   - Gabriel Garabedian
   - Federico Carreño
   - Fabrizzio Crescini
 
## Plataforma para gimnasios:
El proyecto simula una plataforma online inspirada en las grandes cadenas, donde podremos permitir al staff crear rutinas y a su vez al usuario poder tenerlas en sus móviles para poder ver las rutinas, horarios del gym, etc.

Cosas que se pueden hacer:

- Se puede crear, actualizar y borrar publicaciones de rutina, siendo profe logueado con permisos por ser staff del gym.
- Un usuario sin registrar puede solo ver una sola rutina y al volver a la lista
- ✨Podemos ver el horario y dias de apertura, que puede modificarse desde el admin.

Para ello se debe primero checkear la version de Python.

El proyecto fue realizado sobre Python 3.10.6 , por lo que se sugiere utilizar este o una version superior

Para ello debemos poner en windos en el CMD :
- C:\> py --version

O en el shell de Django:
- python --version

En Lynux o MAC:
-$ python --version

Si les aparece la versión correcta pueden seguir. Caso contrario descargar python desde este [link](https://www.python.org/downloads/).

## Instalar:(dependecias pip)

El orden de instalacion de las dependecias, se debe correr [pip.install](pip.install), debemos asegurarnos de estar ubicados en la carperta correspondiente

```ps
 C:\> pip.install django
```

este último instalara django
El comando que se encuentra debajo nos permite verificar la version de Django instalada
```Python
C:\>  python -c "import django; print(django.VERSION)"
```
Se instalaron las depedencias de whitenoise para cargar y alojar imagenes en un servidor local
```Python
C:\>  pip install whitenoise
```
el otro paquete es para trabajar con ellas :(pillow)
```Python
C:\>  pip install Pillow
```

# Configuracion de la Aplicación:
Una vez todo instalado debemos hacer la migracion

en el shell debemos escribir:

```Python
C:\>  python manage.py migrate
```
La consola mostrara las migraciones de la base de datos que se realizaron
## Probando el servidor:

Para probar el servidor debemos correr el siguiente comando
```python
C:\> python manage.py runserver
```

ahora Hace click en el siguiente link para ver el server corriendo: 

[http://localhost:8000/](http://localhost:8000/)

 ```sh
127.0.0.1:8000
```






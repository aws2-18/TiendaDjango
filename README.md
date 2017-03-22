Introduccion
============
Con esta aplicación puedes añadir productos a un carrito y ademas puedes abrir y cerrar carritos, con lo cual puedes tener todos los que quieras.

Guia de instalación
============
Te bajas el repositorio, activas el source, haces un python manage.py migrate, y un python manage.py makemigrations, y lo ejecutas con python manage.pt runserver

Agradecimientos
============
A nuestro profesor Enriz Mieza, por facilitarnos la base de la tienda y facilitarnos la información para subir el proyecto a heroku.
[Link a su repositorio de github](https://github.com/emieza)

App funcionando en prueba
============
[Link a heroku](https://premiumsport.herokuapp.com/)

Como cambiar contraseña del admin del backend
============
Abrimos la shell del usuario con:
python manage.py shell
from django.contrib.auth.models import User
user = User.objects.get(username="admin")
user.set_password("nueva contraseña")
user.save()


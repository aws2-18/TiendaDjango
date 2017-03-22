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
1. This library converts the raw markup to HTML. See the list of [supported markup formats](#markups) below.
1. The HTML is sanitized, aggressively removing things that could harm you and your kin—such as `script` tags, inline-styles, and `class` or `id` attributes. See the [sanitization filter](https://github.com/jch/html-pipeline/blob/master/lib/html/pipeline/sanitization_filter.rb) for the full whitelist.
1. Syntax highlighting is performed on code blocks. See [github/linguist](https://github.com/github/linguist#syntax-highlighting) for more information about syntax highlighting.
1. The HTML is passed through other filters in the [html-pipeline](https://github.com/jch/html-pipeline) that add special sauce, such as [emoji](https://github.com/jch/html-pipeline/blob/master/lib/html/pipeline/emoji_filter.rb), [task lists](https://github.com/github/task_list/blob/master/lib/task_list/filter.rb), [named anchors](https://github.com/jch/html-pipeline/blob/master/lib/html/pipeline/toc_filter.rb), [CDN caching for images](https://github.com/jch/html-pipeline/blob/master/lib/html/pipeline/camo_filter.rb), and  [autolinking](https://github.com/jch/html-pipeline/blob/master/lib/html/pipeline/autolink_filter.rb).
1. The resulting HTML is rendered on GitHub.com


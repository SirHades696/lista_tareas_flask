# To Do List App
## Lista de Tareas con Flask

Aplicación web sencilla que se encarga de crear lista de tareas en forma de stick notes para mejorar la visualización del usuario.

Esta aplicación se encuentra ligada a una BD en MySQL gracias a WSL con Ubuntu.

Esta aplicación esta desarrollada con Flask.

# Preperación del Entorno
Antes de iniciar la ejecución de la aplicación es necesario dar de alta las variables del entorno.
Para que la aplicación funcione, Flask debe reconocer estas variables.
Las variables de entorno se encuentran especificadas dentro del archivo: `__init__.py`

Donde:

> `FLASK_APP` : Es el nombre de la aplicación, en este caso es el nombre que contiene toda la app, la carpeta 'to_do'.
"

> `FLASK_ENV` : En caso de solo usar al aplicación como modo desarrollo.

> `FLASK_DATABASE_HOST` : Nombre o IP para acceder a la Base de Datos.

> `FLASK_DATABASE_PASSWORD` : Contraseña para acceder a la Base de Datos.

> `FLASK_DATABASE_USER` : Usuario para acceder a la Base de Datos.

> `FLASK_DATABASE` : Nombre de la Base de Datos.

En caso de ser la primera vez en usar la aplicación es necesario ejecutar el comando:

> `flask init-db` : Este comando ha sido dado de alta en `db.py` y contiene los esquemas necesarios para purgar, limpiar e inicilizar la Base de Datos.

Este comando solo debe ser ejecutado la primera vez ya que de lo contrario cada que sea llamado realizará las acciones mencionadas con anterioridad.

# ¿Qué Packages son necesarios?
Todos los recursos usados para el desarrollo del bot se encuentran en: `requirements.txt`
> `pip install -r requirements.txt`

# Interactuando con la aplicación web

<img src="to_do\doc\test_web_app.gif">

# Recursos
Flask: https://flask.palletsprojects.com/en/2.0.x/

Secrets: https://docs.python.org/3/library/secrets.html

MySQL Connector: https://dev.mysql.com/doc/connector-python/en/

Click: https://click.palletsprojects.com/en/8.0.x/

Werkzeug: https://werkzeug.palletsprojects.com/en/2.0.x/

Stick Notes Animation: https://code.tutsplus.com/tutorials/create-a-sticky-note-effect-in-5-easy-steps-with-css3-and-html5--net-13934

Icons: https://www.flaticon.com/authors/sbts2018/blue

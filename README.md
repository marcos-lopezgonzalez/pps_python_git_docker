pps_python_git_docker
Vamos a simular la creación de una aplicación web sencilla llamada “La
Bayeta de la Fortuna”. Cada vez que accedamos a la web, nos dirá un
texto auspicioso aleatorio.

app.py
Este archivo crea una aplicación web mediante la librería Flask. Esta apliación tiene 2 endpoints.
Se encuentra alojada en la dirección 127.0.0.1:5000. Para acceder en el navegador ponemos 'http://127.0.0.1:5000'
El endpoint raíz '/' muestra la cadena 'Hola, mundo'.
El endpoint '/frotar/n' devuelve un número n de frases de la galleta de la fortuna.
Implementa los métodos de bayeta.py.

bayeta.py
Define la función frotar. Esta recibe como parámetro un entero 'n_frases'. Por defecto es 1.
El método frotar lee del fichero frases.txt las frases almacenadas. De estas selecciona
el número pasado por parámetro al azar (uso de la librería random) y devuelve una lista con
las frases.

prueba_mongo.py
Archivo en el que se proporcionan las herramientes para la conexión con la base de datos MongoDB.
Contiene un método de instanciación, para inicializar la colección de la base de datos en caso de 
que esté vacía (usa las frases de 'frases.txt'), para borrar la coleccióm y para obtener un número
de frases de la colección mediante una consulta.

Pasos:
- Creamos un entorno virtual con 'python3 -m venv <nombre_entorno>' (En mi caso 'bayeta')
  Tener en cuenta el fichero requirements.txt para la resolución de dependencias.
  Para exportar las dependencias usar 'pip freeze > requirements.txt'

Despliegue seguro con Docker
Se ha implementado el uso de Docker para el despliegue de nuestra aplicación. Para ello se han
creado los ficheros Dockerfile y .dockerignore. Para desplegar nuestra aplicación ahora debemos
realizar lo siguiente:

Creamos una red para nuestros contenedores de Docker (en este ejemplo usaré la red 100.0.0.0/24):
- docker network create --subnet=100.0.0.0/24 <nombre_red>

Creamos la imagen:	
- docker build -t <nombre_repositorio>:<tag> .
  
Para las imagenes:
- docker images
  
Ponemos en marcha el contenedor de la app de la bayeta a través de su imagen:
- docker run -d --network=<nombre_red> --ip 100.0.0.2 -p 5000:5000 --name <nombre_contenedor_app_bayeta> <nombre_repositorio>

Ponemos en marcha el contenedor de mongodb a través de su imagen:
- docker run -d --network=<nombre_red> --ip 100.0.0.3 -p 27017:27017 --name mongo_db mongo
- Si por algún motivo cambias el nombre del contenedor recuerda cambiarlo también en la cadena de conexión del fichero prueba_mongo.py
  
Con estos comandos lanzamos los contenedores en segundo plano, para no bloquear la terminal actual, esto no nos dejará ver los logs
al momento, por lo que debemos usar 'docker logs <nombre_contenedor>'. Sin embargo, si quitamos la opción -d y usamos la opción -it
se bloqueará la terminal actual hasta que paremos el contenedor, pero podremos ver los logs.

Ahora que ya tenemos nuestros dos contenedores funcionando y dentro de una misma red podemos hacer uso de nuestra apliación de la forma
que ya mencioné anteriormente. Por ejemplo:
- curl http://127.0.0.1:5000 nos devolverá la cadena 'Hola, mundo'
- curl http://127.0.0.1:5000/frotar/n, donde 'n' es un número entero, nos devolverá 'n' frases aleatorias.

Despliegue con Docker-Compose:

Para realizar un despliegue más eficaz y sencillo de la apliación se ha implementado docker-compose. De esta forma nos ahorramos tener
que ejecutar todos los comandos mencionados anteriormente cada vez que se quiera iniciar la apliación. Para ello se ha creado el fichero
'docker-compose.yml'. Con el siguiente comando levantamos los dos contenedores:
- docker compose up

# pps_python_git_docker
Vamos a simular la creación de una aplicación web sencilla llamada “La
Bayeta de la Fortuna”. Cada vez que accedamos a la web, nos dirá un
texto auspicioso aleatorio.

#Pasos
Creamos un entorno virtual con 'python3 -m venv bayeta'
Tener en cuenta el fichero requirements.txt para la resolución de dependencias.

#app.py
Este archivo crea una aplicación web mediante la librería Flask. Esta apliación tiene 2 endpoints.
Se encuentra alojada en la dirección 127.0.0.1:5000. Para acceder en el navegador ponemos 'http://127.0.0.1:5000'
El endpoint raíz '/' muestra la cadena 'Hola, mundo'.
El endpoint '/frotar/n' devuelve un número n de frases de la galleta de la fortuna.
Implementa los métodos de bayeta.py.

#bayeta.py
Define la función frotar. Esta recibe como parámetro un entero 'n_frases'. Por defecto es 1.
El método frotar lee del fichero frases.txt las frases almacenadas. De estas selecciona
el número pasado por parámetro al azar (uso de la librería random) y devuelve una lista con
las frases.

#Usamos python:slim
FROM python:slim AS builder

#Establecemos el directorio dentro del contenedor
WORKDIR /app

#Copiamos los archivos necesarios
COPY . /app

#Instalamos las dependencias
RUN pip install --no-cache-dir -r "requirements.txt"

#Puerto 5000
EXPOSE 5000

CMD python ./app.py

#Primero se indica desde que version parte este contenedor
FROM python:3.10 

#Se crea una carpeta dentro del contenedor
WORKDIR /app
#Una buena práctica es copiar el requierements.txt aquí
COPY requirements.txt /app/requirements.txt
#Se pueden instalar las dependencias, se indica que no se quiere la cache y se hace un upgrade a las depndcias si se encuentra
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
#Se hace un copy  de todo el código en la carpeta app, hay que tener cuidado con los espacios
COPY . /app
#Se pone este comando para lanzar el servidor de uvicorn y tener prendido el web server
#CMD ["uvicorn", "main:app","--host", "0.0.0.0", "--port", "80"]
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
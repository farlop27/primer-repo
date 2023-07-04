#Primero se indica desde que version parte este contenedor
FROM python:3.9 

#Se crea una carpeta dentro del contenedor
WORKDIR /app
#Una buena práctica es copiar el requierements.txt aquí
COPY requirements.txt /app/requirements.txt
#Se pueden instalar las dependencias, se indica que no se quiere la cache y se hace un upgrade a las depndcias si se encuentra
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
#Se hace un copy  de todo el código en la carpeta app, hay que tener cuidado con los espacios
COPY . /app
#Se pone este comando para mantener encendido el contenedor
CMD bash -c "while true; do sleep 1; done"
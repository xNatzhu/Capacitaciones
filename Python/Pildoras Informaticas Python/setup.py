#Este archivo setup -> setap / que va contener una descripcion del paquete que vamos destrubuir

#Con la informacion que va tener:

# El nombre del paquete

# La version

# La descripcion - quien es el autor - informacion mas.

from setuptools import setup # primera intruccion

#setup y se le agrega tools import el nombre del archivo setup.

setup( #creamos una funcion setup

# dentro de la funcion se le agrega todo los datos de configuracion.

    name="PaqueteNombre", # -> Aca se le pone el nombre del paquete.
    version="1.0",  #-> aca iria la version del programa
    description="Paquete de prueba y aprendiendo", # -> Aca se explica brevemente para que sirve el paquete
    author="Agustin Saravia xNatzhu", # -> Aca se pone el autor quien creo este paquete
    author_email="agustinnahuelsaravia@gmail.com", # -> Aca sirve para poner el email del autor.
    url="www.prueba.com", # -> La url de referencia

    packages=["paquetes", "paquetes.Subpaquetes"] # -> Aqui se indica donde se encuentra el paquete o el subpaquete que se va empaquetar
    # el primer "," se agrega el paquete, se coloca [el nombre de la carpeta donde esta el paquete en este caso se llama paquetes] y en el segundo agregamos el Subpaquete que para poder añadirlo se debe hacer de la siguiente manera

    #carpeta donde se encuentra . nombre de la carpeta que se llama ese subpaquete.
)


#   ARCHIVOS EXTERNOS.

# El obetivo de trabajar con archivos externos es la persistencia de datos.

#¿Que es? La posibilidad de guardar los datos de tu aplicacion de python que estas utilizando/programando para que no se pierdan.

# Para eso tenemos dos alternativa

# Manejo de archivos externos

# Manejo con BBDD


#MANEJO DE ARCHIVOS EXTERNOS.

# FASES 4

# 1. Crear un archivo externo 

# 2. Una vez que se crea el archivo externo hay que abrirlo (APERTURA)

# 3. Una vez que esta abierto manipularemos ese archivo.

# 4. Cuando este toda la manipulacion realizada lo cerraremos.



#LO PRIMERO QUE VAMOS HACER ES IMPORTAR EL MODULO

#importamos la libreria io --- Y importamos el metodo Open.


from io import open
#FASE CREACION
#FASE APERTURA (SON DOS FASES EN UNA)
archivo_text=open("archivo.txt","w")

#De esta manera podremos abrir un archivo, creamos una variable para almacenar, le ponemos que valdra open() el metodo que usaremos.

# Y el metodo open pedira dos argumentos para poder abrir el archivo externo

# 1. Nombre del archivo externo que queremos abrir
# 2. Y el modo que el archivo se va abrir. El archivo se puede abrir de diferentes maneras

        # Lectura -> Permite leer sobre el (r)
        # Escritura -> permite añadir informacion al archivo (w)
        # append -> para agregar informacion un archivo que existe y tiene info en su interior (a)

# EN EL CASO QUE NO EXISTA EL ARCHIVO QUE SE QUIERA ABRIR SE CREA ESE ARCHIVO.

frase = "Estupendo dia para aprender python" 

 # FASE MANIPULACION 

archivo_text.write(frase) #Llamamos la variable donde esta alojada el archivo. Llamamos el metodo de escribir en este caso "write"

# Y le pasamos el contenido al archivo que tendra escrito lo que dice la variable frase.

#FASE DE CIERRE - UNA VEZ MANIPULADO EL ARCHIVO - HAY QUE CERRARLO.
archivo_text.close()
#Cierra el archivo en memoria que se abrio con la variable con open.



#PARA LEER UN ARCHIVO

texto=open("archivo.txt","r")

leerTexto = texto.read()

#readlines() -> Lo que realiza este metodo es leer la informacion linea por linea y lo guarda dentro de una lista.

texto.close()

print(leerTexto)

archivo_texto2=open("archivo.txt","a") # extension, añadir o agregar.

archivo_texto2.write("---Una nueva linea agregada al archivo existente.")

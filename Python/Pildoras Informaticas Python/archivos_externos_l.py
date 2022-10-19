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
        # "r+" -> Es de lectura y escritura
        

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


archivo_texto2.close()
#       -------------------------------- -------ARCHIVOS EXTERNOS 2------------------


print("-----------------------------Archivo externo 2-------------------------------")

# Cuando le decimos open a un archivo el puntero se ponte en el principio esperando la orden, el puntero es lo mismo que el cursor.

#Al ser una primera lectura el curso se situa al final, esto implica que no puede volver de leer de nuevo una segunda vez al menos que se mueva ese puntero/cursor.

# MODIFICACION DE LA POSICION DEL PUNTERO

# Esto se puede realizar por el metodo seek(numero de caracter donde queremos que se posicione)

archivo_text3 = open("archivo.txt", "r")
print(archivo_text3.read())

archivo_text3.seek(0) # Le decimos que desplace el puntero al principio y pedimos con el read de abajo que haga nuevamente la lectura.

# Seek solamente posiciona el puntero

print(archivo_text3.read(5)) # read hace una lectura hasta el puntero donde estemos.

# Por ejemplo si le decimos read(5) nos va tomar las 5 primeras palabra de la frase, ya que le damos una cantidad hasta donde queremos llegar con el puntero.

archivo_text3.close()

archivo_text4 = open("archivo.txt", "r+")

lista_texto = archivo_text4.readlines()
lista_texto[0]="Esta linea ha sido incluida en el exterior"

archivo_text4.seek(0)

archivo_text4.writelines(lista_texto)

archivo_text4.close()




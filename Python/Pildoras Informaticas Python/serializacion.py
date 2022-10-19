#Serializacion de colecciones, objetos.

# Esta serializacion esta muy vinculado con el tema del manejo de ficheros externos que hemos trabajado anteriormente.

# Que es la serializacion?

# La serializaicon consiste en guardar en un fichero externo (una coleccion, objeto o lista)

# La particularidad que se va guardar en un fichero externo codificado en lenguaje maquina es decir codigo binario. 010101100100

# El proporcito de su uso puede ser:

# Queremos distribuir un objeto construido en py por internet - viene bien porque la distribuccion por medio de internet se hace mas facil.

# Si queremos guardar un script de python en un dispositivo de almacenamiento

# Cuando queremos guardar en una base de datos.

# Para esto vamos utilizar una biblioteca especial para llevar a cabo "Picle"

# Ya que nos permitira utilizar dos metodos que seran muy importante para su uso

# load() -> carga de los datos del fechero binario externo

# dump() -> volcado de datos al fichero binario externo

#EJEMPLO:

import pickle

list_name = ["Pedro", "Juan", "Maria"]

ficheroExterno = open("lista_nombre_serializacion", "wb") #escritura binaria / escritura = w / binaria =b

#Volcado la lista al fichero externo

pickle.dump(list_name, ficheroExterno ) # esto permite crear un guardado/volcado de datos.

ficheroExterno.close()

#Para borrarlo de la memoria se utiliza el metodo del

del(ficheroExterno)

ficheroExterno2 = open("lista_nombre_serializacion", "rb") #read binary = "leera el binario"

lista = pickle.load(ficheroExterno2) # Carga la informacion/mostrar la informacion.

print(lista)
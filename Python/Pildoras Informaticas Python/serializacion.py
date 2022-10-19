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


# SERIALIZAR OBJETOS


class Vehiculos():
    def __init__(self, marca, modelo): #constructor
        
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False
    
    def arrancar(self):
        self.enmarcha = True

    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frena = True
        
    def estado(self):
        print("Marca; ", self.marca, " modelo: ", self.modelo, "en marcha: ", self.enmarcha, "¿el vehiculo se encuentra frenado?", self.frena, "¿El vehiculo acelera?", self.acelera)



coche1 = Vehiculos("Marca 1", "Modelo 1")

coche2 = Vehiculos("Marca 2", "Modelo 2")

coche3 = Vehiculos("Marca 3", "Modelo 3")

#Para no estar seriarizando uno en uno cada objeto creado que se ha inicializado, sino que los vamso a meter una lista esto permitira que podamos hacerlo de una forma mas rapida.

coches= [coche1, coche2, coche3]
ficheroExterno3 = open("Ejercicio_de_serializacion_coches", "wb")

pickle.dump(coches, ficheroExterno3)

ficheroExterno3.close()

del (ficheroExterno3) #Una vez finalizado se puede borrar ese fichero de la memoria, porque ya se encuentra alojado en el disco duro.


ficheroExterno3Apertura= open("Ejercicio_de_serializacion_coches","rb")

#Para poder visualizar lo que hay adentro vamos a crear una variable

verCochesLista = pickle.load(ficheroExterno3Apertura)

#Para poder observar uno por uno los objetos que se encuentran alojado iteraremos con for

for coches in verCochesLista:
    print(coches.estado())

    #Gracias al llamado metodo podemos ver la informacion.
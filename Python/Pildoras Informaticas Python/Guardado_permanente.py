import pickle

class Persona:
    def __init__(self, nombre, genero, edad): # constructor.
        self.nombre = nombre # propiedad = valor
        self.genero = genero
        self.edad = edad

        print("Se ha creado una persona nueva", self.nombre)

    def __str__(self): # Metodo especial -> STR convierte en cadena de texto la informacion de un objeto.
        # Eso servira para ver la informacion de las personas que guardaremos en un futuro.


        return "{}{}{}".format(self.nombre, self.genero, self.edad)  #Se le aplica esos {}.format un formato es decir los datos que va estar cargando dentro de los corchetes.

    

p1 = Persona("Sandra", "Fem", 29) # inicializador - creacion del nuevo objeto



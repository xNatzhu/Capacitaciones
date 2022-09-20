#DICCIONARIOS.

miDiccionario={
    "Alemania":"Berlin",
    "Francia":"Paris",
    "Reino unido": "Londres",
    "España": "Madrid"
}

miDiccionario["Italia"]="Roma"  # Agregar elementos
print(miDiccionario["Francia"]) # Llamar de un elemento a los diccionarios.

print(miDiccionario)

miTupla=("Azul", "Amarillo", "Naranja", "Violeta")

misElementos={
    miTupla[0]:1,
    miTupla[1]:2,
    miTupla[2]:3,
}
#Aca podemos jugar con las tuplas y tambien podemos jugar los objetos, invocamos las tuplas con un respectivo indice y darle un valor en este caso un valor numerico. 

print(misElementos)

jugadores={
    10:"Messi",
    "Nombre":"Lionel Messi",
    "Equipo": "PSG",
    "Goles": 2000,
}

print(jugadores["Equipo"]) #De esta manera puedo ingresar la clave:valor ingreso a la clave equipo y me va dar el valor que en este caso es el psg.

print(jugadores.keys()) #Me da todas las claves que tiene el objeto.

print(jugadores.values())# Imprime todo los valores que tiene el objeto sacando las claves.

print(len(jugadores)) #Nos brinda la longitud que tiene un objeto.

###############################################################################################################

#BUCLES 

#Es repetir una linea de codigo o varias veces.

# for variable in elemento a recorrer. Esta es la sintesis utilizada para los bucles determinantes.


for variable in [1,2,3]: #Va imprimir 3 veces por la cantidad de elementos que posee la lista.
    print(variable)
    print("Hola")





 
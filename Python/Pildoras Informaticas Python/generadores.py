
#GENERADORES:

#Son estructuras que exraen valores de una funcion, y se almacenan en objetos iterables (que se pueden recorrer). 

#Estos valores se almacenan de uno en uno.

#Cada vez que un generador almacena un valor, esta permanece en un estado pausado hasta que se solicita el siguiente. Esta caracteristica es conocida como suspension de estado.


# yield construye un objeto iterable con el primer valor ejemplo: el primer valor de una lista de pares.

# el generador construye objeto iterables donde se almacenara el primer valor que acaba de recorrer.

# La diferencia que hay en una funcion tradicional es que el generador va devolviendo los datos en uno en uno dentro un objeto generador iterador iterable. Y no de golpe como hace una funcion tradicional.

#¿Para que sirve esto?

# Las funciones tradicionales al interar todo de golpe permite que se ocupe mucha memoria y gaste recursos, mienntras que los generadores al generar uno en uno, los recursos gastados seran especificos y controlados.


#Funcion tradicional 
def generarPares(limites):
    num=1

    miLista=[]

    while num < limites:
        miLista.append(num*2)

        num+=1

    return miLista


print(generarPares(10))


#generador: 

print("Probando generadores: ")

def generarPares2(limites):
    num2=1
    while num2 < limites:
       
       yield num2*2

       num2+=1

devuelvePares = generarPares2(10) #aca se estara almacenando lo que ocurra en el generador de uno en uno.

#Para que nos pueda devolver mas de uno lo que haremos sera usar un ciclo.

print(next(devuelvePares)) #El next permite que se ejecute la siguiente iteraccion.

print(next(devuelvePares)) 
print(next(devuelvePares)) #Aca se ejecutaria 3 veces porque el next fueron 3.

# Otra manera poder ejecutarlo de una maneras mas iterable es por medio de los bucles que va iterar el objeto.


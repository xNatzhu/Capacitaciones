#DICCIONARIOS.

import math


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


for ejemplo in ["Pildoras", "Informaticas", 30]:
    print(ejemplo, end=" ") #Esto permite que cuando se este iterando no haga un salto de linea. El END permite
    #realizar esta accion.

#Variables

contador = 0 
miEmail=input("Introduce tu correo electronico: ")
for i in miEmail: 
    if( i=="@" or i=="."):
        contador+=1

        # Hace una comparativa la variable "i" va comparando 1 con cada palabra del string, cada palabra pasara por el filtro condicional y si es verdadero se le asignara verdadero al email.
       
if(contador == 2):
    print("El email es correcto")
# Una vez que el email fue validado correcto se crea un segundo condicional para filtrar su estado y imprimirlo.

else:
    print("No es correcto")

#FOR - RANGE

for rango in range(5): #El range es el comun de javascript que es for of. permite que puedas colocar dentro de el un rango y ponerle la cantidad que se va duplicar. En este caso seria 5 veces.
    print("Hola mundo")

# Bucle While

#El bucle while es un bucle indeterminado porque no sabes cuantas veces va ejecutar el codigo en su interior

#palabra reservada while condicion:
            #cuerpo del bucle

# cuando la condicion es falsa la ejecucion finalizaria. 

i = 1

#while = "Mientras" que i es = 1 sera menor o igual que 10 ejecutara el codigo.

while i<=10:
    print("Ejecucion"+str(i))
    i+=1 # se conoce como un contador.

print("Termino la ejecucion: ")

#Ejercicio para saber si la edad es correcta. 

ingreseEdad = int(input("Ingrese su edad: "))

while ingreseEdad <=0 or ingreseEdad > 120:
    ingreseEdad = int(input("La edad colocada no es correcta, vuelva colocarla nuevamente: "))

print("La edad colocada es correcta, su edad es: " + str(ingreseEdad))


import math #Le decimos a nuestro script que va importar esta clase.

print("Programa de calculo de raiz cuadrada")
añadeUnNumero = int(input("Ingrese el respectivo numero: "))

intentos = 0
while añadeUnNumero < 0:
    print("No se puede hayar la raiz de un numero negativo: ")

    if (intentos==2):
        print("Has consumido demasiado intentos")
        break #El break permite forzar la salida del bucle.
    
    añadeUnNumero = int(input("Ingrese el respectivo numero de nuevo: "))

    if(añadeUnNumero < 0):
        intentos +=1

if(intentos < 2):
    solucion = math.sqrt(añadeUnNumero)
    print("La raiz cuadrada de " + str(añadeUnNumero) + "es " + str(solucion))


#continue -> ignora esa vuelta de bucle apartir de la lectura continua (por ejemplo en la vuelta 5) y salta a la siguiente vuelta del bucle por ejemplo en este caso a la vuelta 6.

#pass -> devolvue null al bucle. Se suele usar para crear clases nules, o cuando estas desarrollando un bucle y le pone pass para que salga null.

#else -> funciona similar a un condicional. 


for letra in "Python":
    
    if(letra == "h"):
        continue #cuando se encuentra con la letra h ignora esa letra y salta a la siguiente iterracion en este caso "o".

    print("Viendo la letra: " + letra)

nombre = "Pildoras informaticas"

contador = 0
for contadorNombre in nombre:
    if(contadorNombre == " "):
        continue
    contador+=1

print(contador)

#Esta es una de las utilidades que podria tener el continue. Ignorar los espacios para brindar un numero de longitud de texto especifico.    


#PASS

#No es muy utilizada por lo que hace es devolver un null, es como si el bucle no se ejecutara.

#ELSE

palabra = "palabra"
letraSeleccionada = "a"

for detectorDeLetra in palabra:
    if(detectorDeLetra == letraSeleccionada):
       validacionDePalabra = True
       break

else: #Cuando el bucle este vacio, y termine de correr y else le dara el re nombre.
    validacionDePalabra = False

print("La palabra seleccionada: " + str(letraSeleccionada) + "tiene una validacion de: " + str(validacionDePalabra))



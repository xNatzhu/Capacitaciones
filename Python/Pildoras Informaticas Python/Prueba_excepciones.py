def divide():

    try:
        op1 = (float(input("Introduce el primer numero: ")))
        op2 = (float(input("Introduce el segundo numero: ")))

        print("La division es: " + str(op1/op2))

    except ValueError: 
        
        # se pueden agregar todas las excepciones que se desee para capturar un error. Al igual que si no especificas el tipo de error y solamente añades except: va capturar un error de forma general.

        print("El valor introduccido es incorrecto.")

    except ZeroDivisionError:
        print("No se puede dividir entre cero!")

    finally: #permite que siempre se ejecute este codigo sin importar lo transcurrido anteriormente. Ya sea que entre en un except o un try se va ejecutar el finally correspondientemente. "fanaly" (se pronuncia asi)

        print("Calculo finalizado")


divide()

def evaluaEdad(edad):

    if edad < 0:
       
       #hay que especificar el tipo de excepcion que largara  cuando cumpla esa condicion.
       raise TypeError("No se permiten edades negativas") #no solamente podemos declarar que tipo de error queremos que lea, sino tambien nos permite que podemos personalizar un mensaje que se puede enviar a un usuario. Esto es lo importante que tiene raise.
            
        # No se va ejecutar porque hemos provocado el lanzamiento de una excepcion, pero no se controla con un bloque try o excepcion. 

        # Te crea un error.
    if edad < 20:
        return "Eres muy joven"
    elif edad < 40:
        return "Eres joven"

    elif edad < 65:
        return "eres maduro"

    elif edad < 100:
        return "Cuidate..."

print(evaluaEdad(10))


#Lo primero que debemos hacer es importar la clase math para utilizarlo la clase en matematicas.

import math

def calculaRaiz(numero):
    if(numero < 0):
        raise ValueError("El numero no puede ser negativo")

    else:
        return math.sqrt(numero)

#al identificar donde se encuentra el error, lo que podemos hacer es capturarlo con el try.

try:
    op1 = int(input("introduce un numero: "))

except ValueError as ErrorDeNumeroNegativo: #El as te permite dar un alias a ese error capturado.

    print(ErrorDeNumeroNegativo)

print(calculaRaiz(op1))

print("Programa finalizado.")
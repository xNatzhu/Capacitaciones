#PAQUETES

# Los paquetes son directorios donde se almacenaran los modulos relacionados entre si.

# Se aconseja que esten organizados en paquete a la hora de crear modulos

#¿Para que sirve?

# Para organizar y reutilizar los modulos

# Como se crea un paquete?

# Crear una carpeta con un archivo __init__.py.


#Ejemplo 1

def sumar(op1, op2):
    print("El resultado de la suma es: ", op1 + op2)


def resta(op1, op2):
    print("El resultado de la resta es: ", op1 - op2)

def multiplicacion(op1, op2):
    print("El resultado de la multiplicacion es: ", op1 * op2)

def dividir(diviendo, divisor):
     print("El resultado de la division es: ", diviendo / divisor)

def potencia(base, exponente):
    print("El resultado de la potencia es: ", base ** exponente)

def redondear(numero):
    print("El resultado de la redondeacion es: ", round(numero))


#Para poder organizar mas el codigo se pueden crear subpaquetes que se encuentren alojados dentro del paquete principal

#from (carpeta).(Subcarpeta).archivo import *
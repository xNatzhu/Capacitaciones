#Una excepcion es un error durante la ejecuccion de un programa. La sistanxis del codigo es correcta durante la ejecuccion ha ocurrido algo inesperado.

# Son errores que el programa es grande puede ser muy peligroso. 


def divide(num1, num2):
    try: #si es verdadero ejecutara eso
        return num1/num2
    
    except ZeroDivisionError: # de lo contrario que aparezca un error manipulara ese error.
        print("No se puede dividir entre 0")

        return "Operacion erronea"


#este seria un try /catch de javascript es una manipulaciones de error para que el codigo pueda seguir desarrollandose aunque tire un error, se capturara ese error y se manipula.

#Si ingresa cero el usuario se va gestionar un error, pero gracias al try /except se podra manipular ese error.



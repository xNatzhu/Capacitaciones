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
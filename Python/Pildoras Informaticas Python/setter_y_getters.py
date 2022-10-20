#METODOS GET Y SET en python.

class Cuenta():

    def __init__(self, pro, sal, mon):
        self.__propietario = pro
        self.__saldo=sal
        self.__moneda=mon

    #ESTA FORMA YA NO SE UTILIZA. SE UTILIZA EN LOS LENGUAJES COMO JS. PERO EN PYTHON YA NO ES VALIDA.

    #Getter (metodos get)
    def get_saldo(self): #Muestra el valor de la moneda
        return self.__saldo

    #Setter (metodos SET)

    def set_Saldo(self, sal): #Permite modificar el valor de la moneda
        self.__saldo = sal

    #Sirven para modificar propiedades dentro de una clase

    #LA FORMA CORRECTA DE PODER HACER UN GET Y SET es reciclando la misma funcion, sin la necesidad de crear diversas funciones. Esto permite mantener un orden.
    #Esto lo podemos hacer gracias a los decoradores "@"

    @property  # decorador (PARA EL GET DEJA EN property)
    def propietario(self):  # Método Getter
        print('Estamos utilizando el método get')

        return self.__propietario

    @propietario.setter
    def propietario(self, propietarioNombre):  # Método Setter
        print('Estamos utilizando el método set')
        self.__propietario = propietarioNombre

    #De esta manera no hay necesidad de poder crear dos funciones diferentes para mostrar y modificar el resultado. Con una sola y gracias a los decoradores podremos modificarlo


cuenta1 = Cuenta("Agustin", 1200, "Pesos")

print(cuenta1.get_saldo()) #Utilizando de esta manera el get podremos mostrar el valor de la propiedad saldo,  ya que al estar encapsulada no nos permite mostrar el valor llamando esa propiedad.


print(cuenta1.set_Saldo(8000)) #De esa manera podemos cambiar el valor de una propiedad encapsulada por el metodo set.

print(cuenta1.get_saldo()) 

print(cuenta1.propietario) #Al trasformarlo @propiedad la funcion se vuelve propiedad lo que no abra necesidad de agregarle los "()"

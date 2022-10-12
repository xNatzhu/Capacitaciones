# HERENCIAS

print("----------------------------------Herencias-----------------------------------------")


#¿Que es una herencia?

# Se trata de trasladar el comportamiento de herencia de personas que ocurre en la vida real y llevarlo al codigo de programacion con algunas pequeñas diferencias.

# representamos en la vida real herencia con programacion

# EL ABUELO -> (clase 1) clase padre o superclase.

# El padre - > (clase 2) clase padre - subclase - superclase (para la clase 3, 4, 5).

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




class Moto2(Vehiculos): #Dentro del parametro agregaremos la clase que va estar heredando, en este caso Vehiculo de esta manera ya moto podria heredar las propiedades y metodos que posee vehiculo.
    hCaballito = ""

    def caballito(self):
        self.hCaballito = "Voy haciendo caballito"

    def estado(self):
        print("Marca; ", self.marca, " modelo: ", self.modelo, "en marcha: ", self.enmarcha, "¿el vehiculo se encuentra frenado?", self.frena, "¿El vehiculo acelera?", self.acelera, "hace el caballito: ", self.hCaballito) #sobre escribimos el metodo de la clase padre, y le agregamos nuestro metodo.

        #esto se conoce como sobre escritura de metodos.

class Furgoneta(Vehiculos):
    
    def carga(self, cargar):
        self.cargado = cargar

        if(self.cargado):
            return "La furgoneta esta cargada"
        else:
            return "La furgoneta no esta cargada."


class VElectricos():
    def __init__(self): #constructor
        self.autonomia = 100
        
    def cargarEnergia(self):
        self.cargando = True


class BicicletasElectricas(VElectricos, Vehiculos): #esto se lo denomina como herencia multiple es decir que va usar propiedades y metodos tanto de vehiculos como vehiculos electricos. Siempre se le da preferencia a la que esta primera.


    pass

miMoto2 = Moto2("Honda", "ELP") #cuando estamos construyendo un objeto para la clase moto hay que poner, los dos argumentos en este caso "modelo y marca que esta solicitando la clase vehiculo para poder hacer la herencia."
miMoto2.caballito()
miMoto2.estado()


miFurgoneta = Furgoneta("Renault", "Kangoo")


miFurgoneta.estado()
print(miFurgoneta.carga(True))

miBiciElectrica = BicicletasElectricas()


#HERENCIA SUPER....

print("**************************HERENCIA SUPER**********************")


class Persona():

    def __init__(self, nombre, edad, ciudad):

        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad

    def descripcion(self):

        print("Nombre: ", self.nombre, "Edad: ", self.edad, "Lugar de residencia: ", self.ciudad)
        

class Empleado(Persona): #Esto hace que la magia de herencia no solamente tenga los elemento del empleado sino tambien la descripcion de una persona, ya que un empleado tambien es una persona.

    def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado,  ciudad_empleado):
                
                #esto permite agregarle mas argumento para solicitar los datos al constructor padre para cuando le agreguemos los datos lo pueda tomar.

        super().__init__(nombre_empleado, edad_empleado, ciudad_empleado)
        #el super esta llamado a los elementos de la clase padre, que elemento? -> al elemento init.
        self.salario = salario
        self.antiguedad = antiguedad

# PRINCIPIO DE SUSTITUCION. PORQUE UN EMPLEADO SIEMPRE SERA UN EMPLEADO.




Antonio = Empleado(2500, 5500, "Antonio", 20, "España")

Antonio.descripcion()

print(isinstance(Antonio, Empleado)) # Devuelve true si pertenece en una clase en concreto o devuelvo false si no lo es, en este caso devolveria true porque el objeto "Antonio esta creado en la clase empleado que tambien esa vinculada con la clase padre persona las que ambas clases serian true."


Agustin = Persona("Agustin", 23, "Argentina")

Agustin.descripcion()

print(isinstance(Agustin, Empleado)) # Aca dara falso porque Agustin no esta perteneciendo a la clase empleado sino solamente a persona.




 
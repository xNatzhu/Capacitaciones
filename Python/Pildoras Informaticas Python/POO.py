#Programacion orientada a objetos.

# Los programacion orientada a procedimiento son los antiguos de la decada de los 60.

# Algunos lenguajes que manipulann esa programacion: "Fortran", "Cobol", "Basic".

#Desventaja: 

# 1. Las lineas de codigo son muy grandes en aplicaciones complejas. En la programacion POO tambien es complejo sin embargo el complejimiento que lleva la programacion de procedimiento es aun mayor(muy exajerado).

# 2. Estos programas son complejos de discifrar, ya sea para poder descubrir un fallo o ver caracteristicas de ese programa  va tener como resultado algo muy complejo.

# 3. Son pocos reutilizable. Si estas por elaborar un proyecto y a los meses quieres hacer el mismo proyecto, te va ser muy complejo poder re utilizar ese codigo para lograr ese objetivo. Eso significa que todas las aplicaciones que creas en ese lenguaje debes crearla desde cero. Repitidamente sin re utilizar el codigo.

# 4. Si existe un fallo en una linea de codigo, es todo el programa  que caiga. 

# 5. La aparicion del codigo espagueti. "Go sub" "Go to" estas intrucciones sirven para dar saltos en el flujo de la ejecucion del programa. Lo que realiza esta accion es poder hacer un salto de codigo hacia adelante o reversa ignorando todo el codigo intermedia. Esto es lo que se conoce como codigo espagueti.

# 6. Es muy complejo depurar con otros programadores, si tienes que corregir un error es muy complejo realizarlo si lo has realizado otro programador.


# POO "PROGRAMACION ORIENTADA A OBJETOS"

# La programacion POO "programacion orientada objetos" nace para poder quitar o la mayor parte de las descentaja que existia con la programacion orientada a procedimiento, de aqui nace esa programacion. 

#Conciste en trasladar la naturaleza de los objetos de la vida real al codigo de programacion. Como podemos hacer mas sencillo el codigo de programacion de cualquier lenguaje y que sea mas entendible, mas manejable a cualquier programador que se encuentre resolviendo o desarrollando una aplicacion. 
# Que mejor forma de darle a ese lenguaje de programacion el mismo comportamiento que tiene los objetos de la vida real con los cuales estamos ya familiarizado. En la vida real estamos rodeado de objetos, todo es un objeto.

# Sabemos que los objetos en la vida real tienen: un estado, comportamiento(¿Que puede hacer?) y unas propiedades.

# ¿Que es el estado de un objeto?

# El estado de un objeto es como se encuentra ese objeto.

# ¿Cual es el estado de un coche? puede estar parado, puede estar circulando, puede estar aparcado, ect.

# ¿Que propiedades tiene el objeto coche? Tiene un color, tiene un peso, tiene un tamaño.

# ¿Que comportamiento de un coche? un coche puede frenar, puede girar, puede arrancar. Es decir que puede hacer ese objeto, nos estamos refiriendo que puede hacer ese vehiculo.

# Objeto:

    # Tiene propiedades (atributos)
        #Color
        #Peso
        #Alto
        #Largo
        #Caracteristica que identifican ese objeto, ya sea su color, su modelo, su pintura, ect.

    #Tiene un comportamiento (¿Que es capas de hacer?)
        #Arrancar
        #Frenar
        #Girar
        #Acelerar
        #Esto lo vamos denominar metodos que van ser lo que va brindar un comportamiento a un objeto.

    #Se trata de trasladar todo esto de la vida cotidiana al mundo de programacion.

#Ventajas:

    # Se puede didivir el programa en trozos, partes, modulos o clases. Esto se lo denomina modularizacion.

    # El codigo es muy re utilizable, es decir creas hoy un app con este lenguaje de programacion y en futuro si tienes que hacer una app similar, podras re utilizar ese codigo que has realizado en ese dia. Para poder re utilizar el codigo a otra, utilizaremos un concepto llamado herencia.

    # Si existe algun fallo en alguna linea del codigo, el programa continuara con su funcionamiento. Es decir que podemos utilizar las excepciones para capturar los errores.

    # Encapsulamiento.



#CONCEPTO O TERMINOLOGIA DE LA POO.


# Clases -> modelo donde se edactan las caracteristicas comunes de un grupo de objetos.

# Ejemplo podriamos decir que una clase hablando de vehiculos podria ser un chasis, o las ruedas. Que son elementos que se podria poner no solamente a un vehiculo sino a varios y a diferentes marcas.


# LAS CLASE VAN SER LAS CARACTERISTICAS COMUNES QUE VAN A TENER LOS OBJETOS.


# MODULARIZACION -> Una app puede estar commpuesta por varias clases  / si una clase esta fallando en una aplicacion es probable que no caiga, pueda seguir funcionando. Lo que realice esa clase no funcionara pero el programa podra seguir funcionando.

# Encasulapcion -> se le denomina al codigo interno que tiene una clase, o un objeto que el mismo esta encapsulado, no interactua con otros objetos sino que esta protegido el codigo. Es decir la clase 1 nada sabe acerca del funcionamiento o del codigo de la clase 2. Sin embargo de alguna forma estan conectadas todas las clases para que las misma funcionen como equipo pero a la vez cada clase esta encapsulado para que el funcionamiento interno no sea accesible desde afuera.

# ¿Como se conectan las clases que forman parte de un programa? Se conectan con lo que se denomina metodo de acceso. Creando metodos de acceso permite conectar las clases para que pueda funcionar como una unidad o equipo.
# Se puede acceder de una clase a otra para que esten conectada entre si, pero hay ciertas caracteristica que estan encapsulada.


#para acceder a las propiedades y comportamiento (pseudocodigo) se realiza mediante la nomenclatura del punto

#¿Que es?

# miCoche.color="rojo"
# miCoche.peso="1050"



#palabra reservada + nombre de la creacion de clase.

class Coche():

    #Un objeto tenia lo siguiente:

        #Estado
        #Propiedad
        #Comportamiento

    #Estado iniciales -> estas caracteristicas son de fabrica / cuando creamos un objeto inmediatamente se le otorga unos datos predeterminados.

    #Los estados iniciales que tendra una determinada clase, se lo denomina constructor. Es un metodo especial que le da estado inicial a los objetos.

    def __init__(self): #el __init__ las dos barras significa que sera el constructor que tendra una clase. Y dentro de esa funcion constructora ira las propiedades y valores iniciales que se otorgaran. Init significa estado inicial.
      
        self.largoChasis = 250 #Se construyo la primera propiedad de la clase.
        self.anchoChasis = 120
        self.ruedas = 4
        self.enMarcha = False

        

    #los metodos se crean con la palabra def. que se refiere a una funcion.

    def enMovimiento(self, arrancamos): #El objeto perteneciente a la clase, Python nos obliga colocarlo como primer parametro obligatorio. hace referencia al this pór ejemplo en JS. El this hacia referencia al propio objeto sin embargo no nos lo pide ponerlo de parametro aca si.
       
        # le pasamos un parametro donde nos dira si el coche es true o false para determinar si arranco.
        self.enMarcha = arrancamos
        
        if(self.enMarcha):
            return "El coche esta en marcha."
        else:
            return "El coche no se encuentra en marcha."
        
    
    def estado(self):
        print("El coche tiene ", self.ruedas, "Ruedas. Un ancho de ", self.anchoChasis, " y un ancho de ", self.largoChasis)

        #self nombre del objeto / la funcion + variable = valor que tendra.
    
#creando un objeto, instancia o ejemplar.

miCoche = Coche() #instanciar una clase, ejemplar de clase. (todo esto se refiere a lo mismo que es crear un objeto). Una diferencia es que en js se utiliza variable = new clase, y aca es variable = clase sin el new.


print("el largo del coche es: ", miCoche.largoChasis)  #aca podriamos ver y acceder cual es la propiedad su valor que esta teniendo el objeto creado.

#el objeto mi coche viaja y se almacena en self. Hace referencia al objeto Micoche.

#miCoche.enMovimiento = True 

print(miCoche.enMovimiento(True))

miCoche.estado()


print("------------------A continuacion creamos el segundo objeto.-------------------------")


miSegundoCoche = Coche() #Ya se creo la segunda instancia.

print(miCoche.enMovimiento(False))

miSegundoCoche.estado()

# ENCAPSULAMIENTO

#El encapsulamiento hablado anteriormente permite resguardar tu codigo y que no se pueda editar desde afuera es decir que respete los datos registrados que se encuentren dentro de una clase para eso se hace lo siguiente

#s elf.__ruedas = 4 "el añadirle __ estamos encapsulando lo que si decimos fuera de una clase"

# miSegundoCoche.rueda = 5 no va a cambiar a 5 porque el "__" permitira que siempre se respete el valor asignado en la clase y no permitira cambiarlo.










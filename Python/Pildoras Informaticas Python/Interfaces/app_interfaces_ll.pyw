from tkinter import *

raiz = Tk()# llamamos a la clase TK - raiz

#standar library tkinter

raiz.title("Ventana de prueba") #PERMITE AGREGAR UN TITULO A LA VENTANA.



raiz.resizable(1,1) # Eeste metodo permite redireccionar  alto x ancho. Es decir permite que si se quiere expandir la pantalla o no, 1 = true, 0 = false

#(widht, height)



#PARA CAMBIAR EL ICONO DEL PROGRAMA ES NECESARIO TENER UN ARCHIVO .ICO EN TU DIRECTORIO.

#raiz.iconbitmap(r'interfaces\logo.ico')

#nombre del objeto.metodo del TK

#"r" es para que lea la dirección en crudo "nombre_de_carpeta", lo reemplazas por el nombre de tu carpeta que contiene el archivo.ico



#PARA CAMBIAR EL TAMAÑO

#raiz.geometry("800x400") #ancho x alto



raiz.config(bg="#161616") # config una de las cosas puedes hacer es cambiar el color de fondo



#-----------------------------------------------------------------------------------------------

miFrame = Frame() 
#de esta manera se creo el frame
#Este frame hay que añadirlo dentro de la raiz, para añadirlo hay que empaquetarlo para realizar esa accion se debe hacer

#Una vez que creamos el frame hay que empaquetarlo.

#Los frame deben estar en el interior de una raiz, para hacer eso se realiza la empaquetacion.

miFrame.pack() #con esto podemos empaquetarlo. 

#Caracteristicas dentro de pack

#.pack(size="bottom") lo que permite que el frame que va estar empaquetado estara anclado al margen de bottom es decir la parte inferior.

#.pack(anchor="n") La propiedad anchor maneja puntos cardianales es decir poder manipular dos dirreciones utilizamos el size que nos dira en que posicion y el anchor en que punto cardinal queremos agregarlo quedaria de esta manera:

#.pack(size="top" anchor="n")

#.pack(fill="") Esto tambien permite redireccionar el frame en el caso que se le ponga fill="x" anclara hasta en el eje x, caso contrario seria con el "y". Para se pueda notar el cambio utilizamos otra propiedad en conjunto que es .pack(fill="y", expand="True").
#El expand lo que permite basicamente poder expandir el relleno que se declaro al principio, y con rellno nos referimos a fill.

#------------------------------

#BORDES.

#Para cambiar el bordes en el frame se debe utilizar la siguiente propiedad.

#config -> relief el tipo de borde que se espera, bd -> el tamaño de borde que se quiere aplicar.

miFrame.config(relief="solid", bd=35) 

#------------------------------

#CAMBIAR EL CURSO CUANDO INGRESA DENTRO DE UN FRAME.

#Para realizar este cambio se utiliza la propiedad cursor=""

miFrame.config(cursor="pirate")

#PARA CAMBIAR EL ICONO DEL PROGRAMA ES NECESARIO TENER UN ARCHIVO.ICO EN TU DIRECTORIO.

#------------------------------
miFrame.config(bg="red")

#.config nos permite cambiar las caracteristicas del frame.

#Se le da tamañana al frame no la raiz. La raiz se adapta al tamaño proporcionado del frame.

miFrame.config(width="650", height="350")


#---------------------------------------------------------------------------------------------------

#ES NECESARIO QUE SIEMPRE MAIN LOOP ESTE EN ULTIMO LUGAR

raiz.mainloop() # Para que una ventana este en ejecuccion debe estar en un bucle infinito es por ese motivo que se utiliza este metodo. Ya que el usuario hara operaciones y para que pueda leerlo debe estar en consante bucle.







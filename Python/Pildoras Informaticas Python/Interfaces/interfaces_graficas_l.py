from tkinter import *

raiz = Tk()# llamamos a la clase TK

#standar library tkinter

raiz.title("Ventana de prueba") #PERMITE AGREGAR UN TITULO A LA VENTANA.



raiz.resizable(1,0) # Eeste metodo permite redireccionar  alto x ancho. Es decir permite que si se quiere expandir la pantalla o no, 1 = true, 0 = false

#(widht, height)



#PARA CAMBIAR EL ICONO DEL PROGRAMA ES NECESARIO TENER UN ARCHIVO .ICO EN TU DIRECTORIO.

raiz.iconbitmap(r'interfaces\logo.ico')
#nombre del objeto.metodo del TK

#"r" es para que lea la dirección en crudo "nombre_de_carpeta", lo reemplazas por el nombre de tu carpeta que contiene el archivo.ico



#PARA CAMBIAR EL TAMAÑO

raiz.geometry("800x400") #ancho x alto



raiz.config(bg="#161616") # config una de las cosas puedes hacer es cambiar el color de fondo




#ES NECESARIO QUE SIEMPRE MAIN LOOP ESTE EN ULTIMO LUGAR

raiz.mainloop() # Para que una ventana este en ejecuccion debe estar en un bucle infinito es por ese motivo que se utiliza este metodo. Ya que el usuario hara operaciones y para que pueda leerlo debe estar en consante bucle.







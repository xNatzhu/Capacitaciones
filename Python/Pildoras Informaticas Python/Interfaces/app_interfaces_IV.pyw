from tkinter import *

root = Tk()

miFrame = Frame(root, width=1200, height=600)

miFrame.pack()
cuadroTexto = Entry(miFrame) #De esta manera el cuadro de texto permite que pertenezca al frame que creamos y el frame va pertenecer a la raiz.

#cuadroTexto.pack()  El empaquetar permite que se refleje todo los item  y cambios creados dentro del respectivo empaquetamiento.

#El metodo place sirve lo mismo que el pack pero con la diferencia que podemos ubicar donde deseemos el elemento.

cuadroTexto.grid(column=1, row=0)

#Label

nombreLabel= Label(miFrame, text="Nombre:")
#nombreLabel.place(x=50, y=30) esta forma no es lo mas aconsejable de hacer un label, por el tema que puede suporponer o si son igual coordenada empuja el otro widget hacia adelante.


#El mas recomendable es grid porque trabaja mediante grillas.

nombreLabel.grid(column=0, row=0, sticky="e", padx=10, pady=10)


#Cuadro texto y label de apellido
cuadroApellido = Entry(miFrame)
cuadroApellido.grid(column=1, row=2)

apellidoLabel= Label(miFrame, text="Apellido:")
apellidoLabel.grid(column=0, row=2,sticky="e",  padx=10, pady=10)


#Cuadro texto y label de dirreccion.
cuadroDirreccion = Entry(miFrame)
cuadroDirreccion.grid(column=1, row=3)

dirreccionLabel= Label(miFrame, text="Direccion de correo:")
dirreccionLabel.grid(column=0, row=3, sticky="e", padx=10, pady=10)
dirreccionLabel.config(bg="red")


#Cuadro texto y label de contraseña.
cuadroContrasena = Entry(miFrame)
cuadroContrasena.grid(column=1, row=4)

contrasenaLabel= Label(miFrame, text="Contraseña:")
contrasenaLabel.grid(column=0, row=4, sticky="e", padx=10, pady=10)
cuadroContrasena.config(show="*") #Show permite que lo que se inserte en el cuadro de texto se vea con el caracter añadido en el show



#fuente: entry tkinter python

#PROPIEDAD STICKY

#Sticky nos permite especificar si quiero arriba, abajo, ect. Lo que seria la posicion de un elemento. Los valores que admite son: n =norte, s= sur. w = oeste, e= este. Con los puntos cardinales podemos adecuar correctamente la posicion de un elemento.

#Al igual que tienen punto intermedios por ejemplo: ne = noreste, se = sureste, sw= suroeste, nw= noreste.


#PROPIEDAD PAD -> revisar si es mas margin que padding.

#La propiedad pad es el padding. Pero para poder utilizarlo se coloca los puntos cardinales en el pad es decir por ejemplo "pady"

root.mainloop()
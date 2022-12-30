from tkinter import *

root = Tk()

miFrame = Frame(root, width=1200, height=600)

minombre = StringVar() #Con esto le decimos a python que esta variable es una cadena de caracteres.

miFrame.pack()
cuadroTexto = Entry(miFrame, textvariable=minombre) 

#textvariable=minombre lo que permite es asociar ese cuadro de texto con la variable.

cuadroTexto.grid(column=1, row=0)

#Label

nombreLabel= Label(miFrame, text="Nombre:")

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


#Cuadro texto y label de contraseña.
cuadroContrasena = Entry(miFrame)
cuadroContrasena.grid(column=1, row=4)

contrasenaLabel= Label(miFrame, text="Contraseña:")
contrasenaLabel.grid(column=0, row=4, sticky="e", padx=10, pady=10)
cuadroContrasena.config(show="*") 

#Cuadro texto y label de dirreccion.

textoComentario = Text(miFrame, width=16, height=5)
textoComentario.grid(column=1, row=5)


scrollbar = Scrollbar(miFrame, command=textoComentario.yview)
#Aca le decimos que el scroll pertenece a textoComentario, y que ademandas se va visualuzar de manera vertical.



scrollbar.grid(column=2, row=5, sticky="nsew")
#sticky="nsew" se refiere que el scrollbar se adapta al tamaño del text. Y posiciona junto con el texto redactado dentro del cuadro.

#recordar cuando hagamos la vinculacion agregar abajo, ya que sino no va leer el componente.

textoComentario.config(yscrollcommand=scrollbar.set) #Al realizar esto hace que el scrol a medida que escribas hace un efecto de achicado o agrandado.


ComentarioLabel= Label(miFrame, text="Comentarios:")
ComentarioLabel.grid(column=0, row=5, sticky="e", padx=10, pady=10)


#BUTON

def botonCodigo():

    minombre.set("Agustin")
    #Si set es para enviar valores a una variable.
    #El get sirve para obtener informacion de un cuadro de texto.


butonForm = Button(root,text="Enviar", command=botonCodigo)

#Para hacer el boton se enlaza con la clase, se coloca el contenedor padre, y el texto que tendra el requerido boton.

butonForm.pack()

#Intrucciones a los botones: command="" se añade una variable/funsion/clase que tendra la condicion de ese boton a la hora de presionarlo.

root.mainloop()
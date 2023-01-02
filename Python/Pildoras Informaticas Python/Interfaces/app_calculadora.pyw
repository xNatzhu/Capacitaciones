from tkinter import * #exportar liberia

root = Tk() #raiz (body)

miFrame = Frame(root, width=1200, height=600) #frame principal donde estaran los elementos.


#----Pantalla--------

pantalla = Entry(miFrame)

pantalla.grid(column=1, row=1, padx=10, pady=10, columnspan=5)
pantalla.config(background="black", fg="#fff", justify="right")

#Teoria

#colspan= cuando consruyes una tabla una zelda que quiere que sea mas larga d lo normal, cuantas columnas ocupa. En este caso como los botones ocupan 4 columnas entonces le diremos a la pantalla que no ocupe solamente una columna sino que 4.


#------BOTONES--------  

#------FILA 1--------  


boton7 = Button(miFrame,text="7", width=3)
boton7.grid(column=1, row=2)
boton8 = Button(miFrame,text="8", width=3)
boton8.grid(column=2, row=2)
boton9 = Button(miFrame,text="9", width=3)
boton9.grid(column=3, row=2)
botonDiv = Button(miFrame,text="/", width=3)
botonDiv.grid(column=4, row=2)

#------FILA 2--------  

boton4 = Button(miFrame,text="4", width=3)
boton4.grid(column=1, row=3)
boton5 = Button(miFrame,text="5", width=3)
boton5.grid(column=2, row=3)
boton6 = Button(miFrame,text="6", width=3)
boton6.grid(column=3, row=3)
botonMult = Button(miFrame,text="X", width=3)
botonMult.grid(column=4, row=3)

#------FILA 3--------  

boton1 = Button(miFrame,text="1", width=3)
boton1.grid(column=1, row=4)
boton2 = Button(miFrame,text="2", width=3)
boton2.grid(column=2, row=4)
boton3 = Button(miFrame,text="3", width=3)
boton3.grid(column=3, row=4)
botonRest = Button(miFrame,text="-", width=3)
botonRest.grid(column=4, row=4)

#------FILA 4--------  

boton0 = Button(miFrame,text="0", width=3)
boton0.grid(column=1, row=5)
botonComa = Button(miFrame,text=",", width=3)
botonComa.grid(column=2, row=5)
botonIgual = Button(miFrame,text="=", width=3)
botonIgual.grid(column=3, row=5)
botonSuma = Button(miFrame,text="+", width=3)
botonSuma.grid(column=4, row=5)

miFrame.pack()


root.mainloop()
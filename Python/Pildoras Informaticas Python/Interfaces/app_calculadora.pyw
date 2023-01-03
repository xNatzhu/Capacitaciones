from tkinter import * #exportar liberia

root = Tk() #raiz (body)

miFrame = Frame(root, width=1200, height=600) #frame principal donde estaran los elementos.
miFrame.config(background="#e5e5e5")

#-----variables----------

numeroPantalla =StringVar() # lo que permite tener un string de caracteres.



#----Pantalla--------

pantalla = Entry(miFrame, textvariable=numeroPantalla) #se asocia la variable en la pantalla
 
pantalla.grid(column=1, row=1, padx=10, pady=20, columnspan=4,rowspan=2)
pantalla.config(border=0,background="#e5e5e5", fg="black", justify="right",width=32)

#Teoria

#colspan= cuando consruyes una tabla una zelda que quiere que sea mas larga d lo normal, cuantas columnas ocupa. En este caso como los botones ocupan 4 columnas entonces le diremos a la pantalla que no ocupe solamente una columna sino que 4.

#---------funciones--------------------------------

def numPulsado(num):
    numeroPantalla.set(numeroPantalla.get() + num)
     


#------BOTONES-------  

#------FILA 1--------  


boton7 = Button(miFrame,text="7", width=6,height=3,highlightbackground="#fff", highlightthickness = 2, bd=0, command=lambda:numPulsado("7"))
boton7.grid(column=1, row=3,padx=2, pady=2)
boton7.config(background="#fff")

boton8 = Button(miFrame,text="8", width=6,height=3, highlightbackground="#fff", highlightthickness = 2, bd=0, command=lambda:numPulsado("8"))
boton8.grid(column=2, row=3,padx=2, pady=2)
boton8.config(background="#fff")

boton9 = Button(miFrame,text="9", width=6,height=3, highlightbackground="#fff", highlightthickness = 2, bd=0,command=lambda:numPulsado("9"))
boton9.grid(column=3, row=3,padx=2, pady=2)
boton9.config(background="#fff")

botonDiv = Button(miFrame,text="/", width=6,height=3, highlightbackground="#d0d0d0", highlightthickness = 2, bd=0)
botonDiv.grid(column=4, row=3,padx=2, pady=2)
botonDiv.config(background="#d0d0d0")

#------FILA 2--------  

boton4 = Button(miFrame,text="4", width=6,height=3,highlightbackground="#fff", highlightthickness = 2, bd=0, command=lambda:numPulsado("4"))
boton4.grid(column=1, row=4,padx=2, pady=2)
boton4.config(background="#fff")
boton5 = Button(miFrame,text="5", width=6,height=3,highlightbackground="#fff", highlightthickness = 2, bd=0, command=lambda:numPulsado("5"))
boton5.grid(column=2, row=4,padx=2, pady=2)
boton5.config(background="#fff")
boton6 = Button(miFrame,text="6", width=6,height=3,highlightbackground="#fff", highlightthickness = 2, bd=0, command=lambda:numPulsado("6"))
boton6.grid(column=3, row=4,padx=2, pady=2)
boton6.config(background="#fff")
botonMult = Button(miFrame,text="X", width=6,height=3,highlightbackground="#d0d0d0", highlightthickness = 2, bd=0)
botonMult.grid(column=4, row=4,padx=2, pady=2)
botonMult.config(background="#d0d0d0")

#------FILA 3--------  

boton1 = Button(miFrame,text="1", width=6,height=3,highlightbackground="#fff", highlightthickness = 2, bd=0, command=lambda:numPulsado("1"))
boton1.grid(column=1, row=5)
boton1.config(background="#fff")
boton2 = Button(miFrame,text="2", width=6,height=3,highlightbackground="#fff", highlightthickness = 2, bd=0, command=lambda:numPulsado("2"))
boton2.grid(column=2, row=5,padx=2, pady=2)
boton2.config(background="#fff")
boton3 = Button(miFrame,text="3", width=6,height=3,highlightbackground="#fff", highlightthickness = 2, bd=0, command=lambda:numPulsado("3"))
boton3.grid(column=3, row=5,padx=2, pady=2)
boton3.config(background="#fff")
botonRest = Button(miFrame,text="-", width=6,height=3,highlightbackground="#d0d0d0", highlightthickness = 2, bd=0)
botonRest.grid(column=4, row=5,padx=2, pady=2)
botonRest.config(background="#d0d0d0")

#------FILA 4--------  

boton0 = Button(miFrame,text="0", width=6,height=3,highlightbackground="#fff", highlightthickness = 2, bd=0, command=lambda:numPulsado("0"))
boton0.grid(column=1, row=6,padx=2, pady=2)
boton0.config(background="#fff")
botonComa = Button(miFrame,text=",", width=6,height=3,highlightbackground="#fff", highlightthickness = 2, bd=0)
botonComa.grid(column=2, row=6,padx=2, pady=2)
botonComa.config(background="#fff")
botonIgual = Button(miFrame,text="=", width=6,height=3,highlightbackground="#fff", highlightthickness = 2, bd=0)
botonIgual.grid(column=3, row=6,padx=2, pady=2)
botonIgual.config(background="#fff")
botonSuma = Button(miFrame,text="+", width=6,height=3,highlightbackground="#d0d0d0", highlightthickness = 2, bd=0)
botonSuma.grid(column=4, row=6,padx=2, pady=2)
botonSuma.config(background="#d0d0d0")

miFrame.pack()

#Inahibitacion de expasion
root.resizable(0,0)
root.mainloop()
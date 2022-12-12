from tkinter import *

root = Tk()

miFrame = Frame(root, width=500, height=400)

miFrame.pack()

#--------------------------------

#LABEL

#Label es una propiedad que te permite agregar textos estatico dentro de un wigets. No se puede interactuar con este texto.

#Label(contenedor,opcion)

#opcion: Text, anchor, bg, bitmap, bd, font, fg, widht, image, ect.
#Los label se utilizan mas para mostrar texto, pero tambien para mostrar imagen.

#contenedor: Es el frame donde va estar adjuntado este respectivo label.

miLabel = Label(miFrame, text="Prueba, texto estatico", fg="red", font=(50)) #fg =color de la letra

miLabel.place(x=100, y=200)

#El metodo place nos permite ubicar en cualquier lugar en nuestra interfaz grafica mediante unas coordenadas de x y y esto permite agregar el elemento texto en un especifico lugar. Sin contar que tambien respeta el tamaño del frame añadido anteriormente. Por esa manera en este caso no se utilizaria .pack para empaquetarlo, ya que cada elemento nuevo siempre hay que empaquetar, en este caso el .pack se remplaza por place.

#Una manera de abreviar el codigo si no se va utilizar para otra cosa. es realizarlo de la siguiente manera.
#Label(MiFrame, text="sqew").place(x=50, y=50)



root.mainloop()
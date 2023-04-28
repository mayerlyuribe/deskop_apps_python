#-----------------------------
# desktop app No 1.
#-----------------------------

#se importa la libreria tiknter con todas sus funcones
from tkinter import *
#-----------------------------
# funciones de la app
#-----------------------------

#-----------------------------
# ventana principal de la app
#-----------------------------

#se decalara una variable llamada ventana principal que adquiere las caracteristicas de un objeto TK()
ventana_principal=Tk()

#titulo de la ventana
ventana_principal.title("bandera de colombia")

#tamaño de la ventana

ventana_principal.geometry(("500x500"))

#deshabilitar botón de maximizar
ventana_principal.resizable(False,False)
#color de fondo de la ventana
ventana_principal.config(bg="burlywood2")

#------------------------------------
#frame amarillo
#------------------------------------
frame_amarillo =Frame(ventana_principal)
frame_amarillo.config(bg="yellow", width=500, height=250)
frame_amarillo.place(x=0 , y=0)


#------------------------------------
#frame azul
#------------------------------------
frame_azul=Frame (ventana_principal)
frame_azul.config(bg="blue", width=500, height=125)
frame_azul.place(x=0 , y=250)


#------------------------------------
#frame rojo
#------------------------------------
frame_amarillo =Frame(ventana_principal)
frame_amarillo.config(bg="red", width=500, height=125)
frame_amarillo.place (x=0 , y=375)


#run
#se ejecuta el metodo mainloop () de la clase TK() a travez de la instancia de la ventana_principal. este metodo despliega la ventana en pantalla y queda a la espera de lo que el usuario haga(clik en un botón escribir etc.) cada accion de el usuario se conoce como un evento.el metodo mainloop() es un bucle infinito
ventana_principal.mainloop()

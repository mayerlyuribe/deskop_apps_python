#-----------------------------
#bandera de francia
#-----------------------------
from tkinter import*

ventana_principal=Tk()

#titulo de la ventana
ventana_principal.title("bandera")
ventana_principal.geometry(("500x500"))

#deshabilitar botón de maximizar
ventana_principal.resizable(False,False)
ventana_principal.config(bg="burlywood2")

#------------------------------------
#frame amarillo
#------------------------------------
frame_amarillo=Frame(ventana_principal)
frame_amarillo.config(bg="yellow", width=500, height=250)
frame_amarillo.place(x=0, y=125)

#------------------------------------
#frame rojo
#------------------------------------
frame_rojo=Frame(ventana_principal)
frame_rojo.config(bg="red", width=500, height=125)
frame_rojo.place(x=0, y=0)

#------------------------------------
#frame rojo
#------------------------------------
frame_rojo=Frame(ventana_principal)
frame_rojo.config(bg="red", width=500, height=125)
frame_rojo.place(x=0, y=375)

#------------------------------------
#frame rojom
#------------------------------------
frame_rojom= Frame(ventana_principal)
frame_rojom.config(bg="red", width=100, height=100)
frame_rojom.place(x=10, y=200)

ventana_principal.mainloop()
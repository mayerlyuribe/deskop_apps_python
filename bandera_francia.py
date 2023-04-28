#-----------------------------
#bandera de francia
#-----------------------------
from tkinter import*

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
#frame azul
#------------------------------------
frame_azul =Frame(ventana_principal)
frame_azul.config(bg="blue", width=166, height=500)
frame_azul.place(x=0 , y=0)

#------------------------------------
#frame blanco
#------------------------------------
frame_blanco =Frame(ventana_principal)
frame_blanco.config(bg="white", width=166, height=500)
frame_blanco.place(x=166 , y=0)
#------------------------------------
#frame rojo
#------------------------------------
frame_rojo=Frame(ventana_principal)
frame_rojo.config(bg="red3", width=168, height=500)
frame_rojo.place(x=332, y=0)



ventana_principal.mainloop()



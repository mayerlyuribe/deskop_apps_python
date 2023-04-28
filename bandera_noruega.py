#-----------------------------
#bandera de noruega
#-----------------------------
from tkinter import*

ventana_principal=Tk()

#titulo de la ventana
ventana_principal.title("bandera de noruega")

#tamaño de la ventana
ventana_principal.geometry(("700x500"))

#deshabilitar botón de maximizar
ventana_principal.resizable(False,False)
#color de fondo de la ventana
ventana_principal.config(bg="black")
#------------------------------------
#frame rojo
#------------------------------------
frame_rojo=Frame(ventana_principal)
frame_rojo.config(bg="red3", width=700, height=500)
frame_rojo.place(x=0, y=0)
#------------------------------------
#frame blanco
#------------------------------------
frame_blanco=Frame(ventana_principal)
frame_blanco.config(bg="white", width=100, height=700)
frame_blanco.place(x=180, y=0)

#------------------------------------
#frame blanco
#------------------------------------
frame_blanco=Frame(ventana_principal)
frame_blanco.config(bg="white", width=700, height=100)
frame_blanco.place(x=0, y=200)

#------------------------------------
#frame azul1
#------------------------------------
frame_blanco=Frame(ventana_principal)
frame_blanco.config(bg="navy", width=50, height=700)
frame_blanco.place(x=205, y=0)


#------------------------------------
#frame azul2
#------------------------------------
frame_azul=Frame(ventana_principal)
frame_azul.config(bg="navy", width=700, height=50)
frame_azul.place(x=0, y=225)
ventana_principal.mainloop()
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
ventana_principal.config(bg="red")

ventana_principal.mainloop()

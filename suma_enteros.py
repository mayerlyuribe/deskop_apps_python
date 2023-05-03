#----------------------
#suma enteros
#----------------------
from tkinter import*
from tkinter import messagebox

#-----------------------------
# funciones de la app
#-----------------------------

def calcular():
    messagebox.showinfo("minicalculadora 1.0", "las operaciones han sido realizadas")
    s = int(x.get()) + int (y.get())
    r = int(x.get()) - int (y.get())
    m = int(x.get()) * int (y.get())
    d = int(x.get()) / int (y.get())
    de = int(x.get()) // int (y.get())
    mod  = int(x.get()) % int (y.get())
    p = int(x.get()) * int (y.get())
    t_resultados.insert(INSERT, f"{int(x.get())} + {int(y.get())} = {s}")
    t_resultados.insert(INSERT, f"\n{int(x.get())} - {int(y.get())} = {r}")
    t_resultados.insert(INSERT, f"\n{int(x.get())} * {int(y.get())} = {m}")
    t_resultados.insert(INSERT, f"\n{int(x.get())} / {int(y.get())} = {d}")
    t_resultados.insert(INSERT, f"\n{int(x.get())} // {int(y.get())} = {de}")
    t_resultados.insert(INSERT, f"\n{int(x.get())} % {int(y.get())} = {mod}")
    t_resultados.insert(INSERT, f"\n{int(x.get())} ** {int(y.get())} = {p}")


def borrar(): 
    messagebox.showinfo("minicalculadora 1.0, los datos serán borrrados")
    x.set("")
    y.set("")
    t_resultados.delete("1.0","end")


def salir():
    messagebox.showinfo("minicalculadora 1.0", "El programa se cerrará")
    ventana_principal.destroy()

ventana_principal=Tk()
ventana_principal.title("suma enteros")
ventana_principal.geometry(("500x500"))
ventana_principal.config(bg="dark olive green", width=480, height=180)

#variables globales

x=StringVar()
y=StringVar()


#----------------------
#entrada de datos
#----------------------
frame_entrada=Frame (ventana_principal)
frame_entrada.config(bg="white", width=480, height=180)
frame_entrada.place(x=10, y=10)

#-----------------------
# logo de la app
#-----------------------
logo = PhotoImage(file="img/escudo_colegio.png")
lb_logo = Label(frame_entrada, image=logo, bg="white")
lb_logo.place(x=70, y=40)
#-----------------------
# titulo de la app
#-----------------------
titulo=Label(frame_entrada, text="minicalculadora 1.0")
titulo.config(font=("Helvetica", 16), bg="white", fg="DarkOliveGreen4")
titulo.place(x=140, y=10)

#------------------------
# frame operaciones
#------------------------
frame_operaciones = Frame(ventana_principal)
frame_operaciones = Frame(bg="white", width=480, height=100)
frame_operaciones.place(x=10, y=200)


# boton para sumar
bt_sumar = Button(frame_operaciones, text="Sumar", command=calcular)
bt_sumar.config(font=("Arial", 16), bg="white", fg="navy")
bt_sumar.place(x=45, y=35, width=100, height=30)

# boton para borrar
bt_borrar = Button(frame_operaciones, text="Borrar", command=borrar)
bt_borrar.config(font=("Arial", 16), bg="white", fg="navy")
bt_borrar.place(x=190, y=35, width=100, height=30)

# boton para salir
bt_salir = Button(frame_operaciones, text="Salir", command=salir)
bt_salir.config(font=("Arial", 16), bg="white", fg="navy")
bt_salir.place(x=335, y=35, width=100, height=30)


#------------------------
# frame resultados
#------------------------
frame_resultados = Frame(ventana_principal)
frame_resultados = Frame(bg="white", width=480, height=180)
frame_resultados.place(x=10, y=310)

#-------------------------
#etiqueta para valor de x
#------------------------
lb_x=Label(frame_entrada, text = "x=")
lb_x.config(bg="white", fg="dark green", font="helvetica")
lb_x.place(x=240, y=60)

#------------------------
#caja para valor x
#------------------------
entry_x= Entry(frame_entrada)
entry_x.config(bg="white", fg="DarkOliveGreen4", font=("Tines New Roman", 18), width=6)
entry_x.focus_set()
entry_x.place(x=260, y=58)

#------------------------
#etiqueta para valor de y
#------------------------
lb_y=Label(frame_entrada, text = "y=")
lb_y.config(bg="white", fg="dark green", font="helvetica")
lb_y.place(x=240, y=100)

#------------------------
#caja para valor y
#------------------------
entry_y= Entry(frame_entrada)
entry_y.config(bg="white", fg="DarkOliveGreen4", font=("Times New Roman", 18), width=6)
entry_y.focus_set()
entry_y.place(x=260, y=98)

#boton para sumar
bt_suma = Button(frame_operaciones, text="calcular", command=calcular)
bt_suma.place(x=45, y=35, width=100, height=30)

#boton para borrar
bt_suma = Button(frame_operaciones, text="borrar", command=borrar)
bt_suma.place(x=190, y=35, width=100, height=30)

#boton para salir
bt_suma = Button(frame_operaciones, text="salir", command=salir)
bt_suma.place(x=335, y=35, width=100, height=30)

#area de texto para los resultados
t_resultados= Text(frame_resultados)
t_resultados.config(bg="black",font=("Courier",20), fg="DarkOliveGreen4")
t_resultados.place(x=10, y=10, width=460, height=160)




ventana_principal.mainloop()
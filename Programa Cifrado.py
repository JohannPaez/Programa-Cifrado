from tkinter import * 
from tkinter import messagebox
from archivos import publicKeyCipher, keyGenerator

def center(toplevel):
       toplevel.update_idletasks()
       w = toplevel.winfo_screenwidth()
       h = toplevel.winfo_screenheight()
       size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
       x = w/2 - size[0]/2
       y = h/2 - size[1]/2
       toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))

def generarLlaves():
    keyGenerator.main()

def salir():
    if (messagebox.askyesno(message="¿Está seguro que desea salir?", title="Mensaje")):
        root.destroy()

def cifrar():
    try:
        mensaje = text.get("1.0", "end-1c")
        res = publicKeyCipher.main(mensaje, "1")
        limpiarYMostrarTexto(res)
    except:
        messagebox.showinfo(message="El texto que desea cifrar solo puede contener '!', '?', '.', letras, numeros y espacios.", title="Mensaje")

def decifrar():
    try:
        mensaje = text.get("1.0", "end-1c")
        res = publicKeyCipher.main(mensaje, "2")
        limpiarYMostrarTexto(res)
    except:
        messagebox.showinfo(message="El texto que desea decifrar es incorrecto o no tiene el formato adecuado.", title="Mensaje")
def limpiarYMostrarTexto(mensaje):
    text1.delete("1.0", "end-1c")
    text1.insert(INSERT,mensaje)

def main():
    global root, text, text1
    root = Tk()

    root.geometry("700x700")
    root.title("Welcome to the Chiper")
    center(root)
    #No olvidar colocar fondo nuevamente 'Login fondo.jpg'

    imagenFondo= PhotoImage(file="archivos/imagenFondo.gif")
    LableFondo = Label(root, image=imagenFondo).place(x=0,y=0)

    text = Text(root, height = 6, width = 60)
    text.fieldname = "text"
    text.grid(row = 5, column = 1)

    text1 = Text(root, height = 6, width = 60)
    text1.fieldname = "text1"
    text1.grid(row = 15, column = 10)

    Button(root, text="Cifrar texto", command = cifrar, width = "15").place(x=220, y=288)
    Button(root, text="Decifrar texto", command = decifrar, width = "15").place(x=220, y=318)
    Button(root, text="Salir", command = salir, width = "10").place(x=310, y=530)
    
    text.place(x = 110, y = 170)
    text1.place(x = 110, y = 405)

    generarLlaves()
    root.mainloop()


main()



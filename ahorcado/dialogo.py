import sys
try:
    import tkinter as tk
    from tkinter import ttk
except ImportError:
    print("Se requiere el modulo tkinter. Más información en about.txt")
    sys.exit(1)

class Dialogo(object):

    def __init__(self, master=None, error="Desconocido"):

        self.dialogo = tk.Tk()
        self.dialogo.configure(background="#121")
        self.dialogo.overrideredirect(True)
        self.dialogo.attributes("-topmost", True)
        self.dialogo.focus_set()
        ancho = 450
        alto = 220
        x = (self.dialogo.winfo_screenwidth() // 2) - (ancho // 2)
        y = (self.dialogo.winfo_screenheight() // 2) - (alto // 2)
        self.dialogo.geometry('{}x{}+{}+{}'.format(ancho, alto, x, y))

        self.master = master
        if self.master:
            self.master.withdraw()
            msg = (
                "Misión abortada.\n\nSe ha producido un error\ny la aplicación "
                "se cerrará.\n\nError: {}").format(error)
        else:
            msg = error

        label = tk.Label(
            self.dialogo, text=msg, fg="white", background="#121",
            font=("Helvetica", 14), justify="center")
        label.pack(anchor="center", padx=5, pady=20)

        boton = ttk.Button(self.dialogo, text='Cerrar', command=self.salir)
        boton.bind('<Return>', lambda e: self.dialogo.destroy())
        boton.focus()
        boton.pack(padx=10, pady=5)

        self.dialogo.mainloop()

    def salir(self):
        self.dialogo.destroy()
        if self.master:
            sys.exit(1)

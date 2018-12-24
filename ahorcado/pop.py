import os
import sys
try:
    import tkinter as tk
    from tkinter import ttk
except ImportError:
    print("Se requiere el modulo tkinter. Más información en about.txt")
    sys.exit(1)

#-------------------------------------------------------------------------
# clase: Popup(object)
#-------------------------------------------------------------------------
class Popup(object):

    def __init__(self):
        self.popup = tk.Tk()
        self.popup.configure(background="#121")
        self.popup.overrideredirect(True)

        width = 400
        height = 300
        x = (self.popup.winfo_screenwidth() // 2) - (width // 2)
        y = (self.popup.winfo_screenheight() // 2) - (height // 2)
        self.popup.geometry('{}x{}+{}+{}'.format(width, height, x, y))

        self.popup.attributes("-topmost", True)
        self.popup.focus_set()

        msg = ("\nEL AHORCADO - 0.2.3\n\nEl juego arrancará enseguida,\n"
            "estamos recuperando datos y...")
        label = tk.Label(self.popup, text=msg, fg="white", background="#121",
            font=("Helvetica", 14))
        label.pack(side="top", padx=30, pady=5)

        self.progressbar = ttk.Progressbar(self.popup, length=150,
            mode="indeterminate")
        self.progressbar.pack(padx=30, pady=10)
        self.progressbar.start(10)
        self.popup.after(2000, self.popup.destroy)

        msg = "...preparando la horca"
        label = tk.Label(self.popup, text=msg, fg="white", background="#121",
            font=("Helvetica", 18))
        label.pack(side="top", padx=30, pady=0)

        try:
            soga = tk.PhotoImage(file=os.path.join(os.path.dirname(__file__),
                "resources/img/derrotas.png"))
        except:
            print("ERROR: ARCHIVO NO ENCONTRADO.")
            soga = tk.PhotoImage()
        canvasSoga = tk.Canvas(self.popup, width=64, height=64, bd=0,
            background="#121", highlightthickness=0)
        canvasSoga.create_image(0, 0, anchor="nw", image=soga)
        canvasSoga.pack(side=tk.TOP, expand=False, padx=30, pady=20)

        self.popup.mainloop()

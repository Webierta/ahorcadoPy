import tkinter as tk
from tkinter import ttk
from random import choice
from random import randint
import threading

#-------------------------------------------------------------------------
# clase: Popup(object)
#-------------------------------------------------------------------------

class Popup(object):

    def __init__(self, msg, pX=None, pY=None, tit=None):
        self.popup = tk.Tk()
        self.popup.overrideredirect(1)

        if not pX or not pY:
            sw = self.popup.winfo_screenwidth()
            sh = self.popup.winfo_screenheight()
            pX = str(sw - sh)
            pY = str(int(pX)//2)
        self.popup.geometry("350x150+{}+{}".format(pX, pY))
        self.popup.attributes("-topmost", True)
        self.popup.focus_set()

        label = ttk.Label(self.popup, text=msg, font=("Helvetica", 12))
        label.pack(side="top", pady=20, padx=20)

        if tit == "inicio":
            self.progressbar = ttk.Progressbar(self.popup, length=150,
                mode="indeterminate")
            self.progressbar.pack()
            self.progressbar.start(10)
            self.popup.after(3000, self.popup.destroy)  #3000
        elif tit == "update":
            self.frame = tk.Frame(self.popup)
            self.frame.pack()
            for i in range(randint(6, 10)):
                threading.Thread(target=self.hilo_update).start()
            else:
                self.popup.after(500, self.popup.destroy)

        self.popup.mainloop()

    def hilo_update(self):
        var = tk.StringVar()
        label = tk.Label(self.frame, textvariable=var,
            font=("Courier", 20, "bold"))
        label.pack(side=tk.LEFT, padx=4)
        self.count = 0
        self.update_label(label, var)

    def update_label(self, lbl, var):
        if self.count < 200:
            letras = "____________________AAAABCDEEEEFGHIIIIJKLMNÑOOOOPQRSTUUUUVWXYZ"
            letra = choice(letras)
            var.set(letra)
            mseg= randint(10, 500)
            lbl.after(mseg, lambda: self.update_label(lbl, var))
            self.count += 1

import sys
import os
from subprocess import call
import webbrowser
import threading
try:
    import tkinter as tk
    import tkinter.font as font
    from tkinter import ttk
    from tkinter import scrolledtext
    from tkinter import messagebox
except ImportError:
    print("Se requiere el modulo tkinter. Más información en about.txt")
    sys.exit(1)
from ahorcado.juego import Juego
from ahorcado.datos import Datos
from ahorcado.pop import Popup

files = {
    "help": os.path.join(os.path.dirname(__file__), "resources/txt/HELP.rst"),
    "about": os.path.join(os.path.dirname(__file__), "resources/txt/ABOUT.rst"),
    "titulo": os.path.join(os.path.dirname(__file__), "resources/img/ahorcado.png"),
    "icono": os.path.join(os.path.dirname(__file__), "resources/img/icon128.png"),
    "paypal": os.path.join(os.path.dirname(__file__), "resources/img/donate.gif"),
    "pista": os.path.join(os.path.dirname(__file__), "resources/img/pista.png"),
    "marcador": os.path.join(os.path.dirname(__file__), "resources/img/marcador.png"),
    "triunfos": os.path.join(os.path.dirname(__file__), "resources/img/triunfos.png"),
    "derrotas": os.path.join(os.path.dirname(__file__), "resources/img/derrotas.png"),
    "error": os.path.join(os.path.dirname(__file__), "resources/media/error.wav"),
    "acierto": os.path.join(os.path.dirname(__file__), "resources/media/acierto.wav"),
    "gameover": os.path.join(os.path.dirname(__file__), "resources/media/gameover.wav"),
    "victoria": os.path.join(os.path.dirname(__file__), "resources/media/victoria.wav")
}

#-------------------------------------------------------------------------
# clase: Base()
#-------------------------------------------------------------------------
class Base(object):

    modos = {"Avanzado": 0, "Júnior": 1, "Temas": 2}

    def __init__(self, master):

        self.datos = Datos()

        # Fuentes y estilos
        font.nametofont("TkDefaultFont").configure(family="Helvetica", size=12)
        font.nametofont("TkMenuFont").configure(family="Helvetica", size=12)
        font.nametofont("TkCaptionFont").configure(family="Helvetica", size=12,
            weight="normal")
        ttk.Style().configure('gran.TButton', font=("Helvetica", 18))
        ttk.Style().configure('key.TButton', font=("Helvetica", 16))

        # Ventana
        self.master = master
        self.master.protocol("WM_DELETE_WINDOW", lambda: sys.exit())
        self.master.title("El Ahorcado")
        self.master.configure(background="#121")

        # Menu
        self.menuApp = tk.Menu(self.master, relief=tk.FLAT)
        self.master.config(menu=self.menuApp)
        self.menuGame = tk.Menu(self.menuApp, tearoff=0, bd=2,
            activeborderwidth=2, relief=tk.GROOVE)
        self.menuEdit = tk.Menu(self.menuApp, tearoff=0, bd=2,
            activeborderwidth=2, relief=tk.GROOVE)
        self.menuInfo = tk.Menu(self.menuApp, tearoff=0, bd=2,
            activeborderwidth=2, relief=tk.GROOVE)
        self.menuApp.add_cascade(menu=self.menuGame, label="Juego")
        self.menuApp.add_cascade(menu=self.menuEdit, label="Editar")
        self.menuApp.add_cascade(menu=self.menuInfo, label="Info")

        self.menuGame.add_command(label="Nuevo Juego", underline=0,
            command=lambda: self.cambiar_clase(Game), accelerator="Alt+N")
        self.menuGame.add_command(label="Marcador",
            command=lambda: self.cambiar_clase(Marcador))
        self.menuGame.add_separator()
        self.menuGame.add_command(label="Salir",
            command=sys.exit, accelerator="Alt+Q")
        self.master.bind_all("<Alt-n>", lambda event: self.cambiar_clase(Game))
        self.master.bind_all("<Alt-q>", lambda event: sys.exit())

        self.niveles = tk.Menu(self.menuEdit, tearoff=0,
            bd=2, activeborderwidth=2, relief=tk.GROOVE)
        self.menuEdit.add_cascade(menu=self.niveles, label="Nivel ")
        for clave in self.modos:
            self.niveles.add_command(label=clave, command=lambda arg=clave:
                self.cambiar_nivel(self.niveles, arg))
        self.niveles.entryconfigure(self.modos[self.datos.nivel], state="disabled")

        self.sonido = tk.Menu(self.menuEdit, tearoff=0, bd=2,
            activeborderwidth=2, relief=tk.GROOVE)
        self.menuEdit.add_cascade(menu=self.sonido, label="Sonido ")
        self.sonido.add_command(label="OK",
            command=lambda: self.cambiar_sonido(self.sonido, True))
        self.sonido.add_command(label="Mute",
            command=lambda: self.cambiar_sonido(self.sonido, False))
        entry = 0 if self.datos.sonido else 1
        self.sonido.entryconfigure(entry, state="disabled")

        self.menuInfo.add_command(label="Ayuda",
            command=lambda: self.info(files.get("help", "ERROR")))
        self.menuInfo.add_command(label="Acerca de",
            command=lambda: self.info(files.get("about", "ERROR")))

    def info(self, archivoInfo):
        dialogo = tk.Toplevel(self.master)
        dialogo.resizable(0,0)
        geom = self.master.winfo_geometry()
        pos = geom.split("+")
        pX = str(int(pos[1]) - 1)
        pY = str(int(pos[2]) - 56)
        dialogo.geometry("600x600+{}+{}".format(pX, pY))

        frame_txt = tk.Frame(dialogo)
        text = tk.scrolledtext.ScrolledText(
            frame_txt, wrap="word", font=("Courier", 12))
        try:
            with open(archivoInfo, "r", encoding='utf-8') as archivoOpen:
                txtRead = archivoOpen.read()
        except:
            txtRead = "ERROR. ARCHIVO NO ENCONTRADO."
        text.insert(tk.END, txtRead)
        text.configure(state=tk.DISABLED, padx=10, pady=10)
        text.pack(fill=tk.BOTH, expand=1)
        frame_txt.pack(fill=tk.BOTH, expand=1, side=tk.TOP)

        boton = ttk.Button(dialogo, text='Cerrar', command=dialogo.destroy)
        boton.bind('<Return>', lambda e: dialogo.destroy())
        boton.focus()
        boton.pack(side=tk.BOTTOM, padx=20, pady=20)

        dialogo.focus_set()
        dialogo.grab_set()
        dialogo.transient(self.master)
        self.master.wait_window(dialogo)  #self.dialogo.mainloop()

    def cambiar_clase(self, clase):
        geom = self.master.winfo_geometry()
        pos = geom.split("+")
        pX = str(int(pos[1]) - 1)
        pY = str(int(pos[2]) - 56)
        self.datos.guardar_pantalla(*[pX, pY])

        self.master.destroy()

        ejeX = str(int(self.datos.posicion_x) + 175)
        ejeY = str(int(self.datos.posicion_y) + 250)
        if clase == Game:
            Popup("Generando palabra", ejeX, ejeY, tit="update")
        newRoot = tk.Tk()
        posX = self.datos.posicion_x
        posY = self.datos.posicion_y
        newRoot.geometry("700x700+{}+{}".format(posX, posY))
        clase(newRoot)  # newRoot.mainloop()

    def cambiar_nivel(self, menu, clave):
        for key, value in self.modos.items():
            estado = "disabled" if key == clave else "normal"
            menu.entryconfigure(value, state=estado)
        self.datos.guardar_nivel(clave)

    def cambiar_sonido(self, menu, booleano):
        menu.entryconfigure(int(not booleano), state="disabled")
        menu.entryconfigure(int(booleano), state="normal")
        self.datos.guardar_sonido(booleano)

#-------------------------------------------------------------------------
# clase: StartPage(Base)
#-------------------------------------------------------------------------
class StartPage(Base):

    def __init__(self, master):
        super().__init__(master)
        self.master = master

        try:
            imgTitulo = tk.PhotoImage(file=files["titulo"])
        except:
            print("ERROR: ARCHIVO NO ENCONTRADO.")
            imgTitulo = tk.PhotoImage()
        canvas = tk.Canvas(self.master, width=530, height=48,
            background="#121", bd=0, highlightthickness=0)
        canvas.create_image(0, 0, anchor="nw", image=imgTitulo)
        canvas.pack(side=tk.TOP, expand=False, padx=30, pady=30)

        try:
            imgIcon = tk.PhotoImage(file=files["icono"])
        except:
            print("ERROR: ARCHIVO NO ENCONTRADO.")
            imgIcon = tk.PhotoImage()
        canvasIcon = tk.Canvas(self.master, width=128, height=128,
            background="#121", bd=0, highlightthickness=0)
        canvasIcon.create_image(0, 0, anchor="nw", image=imgIcon)
        canvasIcon.pack(side=tk.TOP, expand=False, padx=30, pady=10)

        btnGame = ttk.Button(self.master, text="Nuevo Juego", width=25,
            style="gran.TButton", command = lambda: self.cambiar_clase(Game))
        btnPunt = ttk.Button(self.master, text="Marcador", width=25,
            style="gran.TButton", command = lambda: self.cambiar_clase(Marcador))

        btnGame.pack(side=tk.TOP, fill=tk.BOTH, padx=30, pady=10, ipady=10)
        btnPunt.pack(side=tk.TOP, fill=tk.BOTH, padx=30, pady=0, ipady=10)

        try:
            imgPaypal = tk.PhotoImage(file=files["paypal"])
        except:
            print("ERROR: ARCHIVO NO ENCONTRADO.")
            imgPaypal = tk.PhotoImage()
        tk.Button(self.master, image=imgPaypal, cursor="hand1", bd=0,
            highlightthickness=0, background="#121", activebackground="#121",
            command=self.paypal).pack(side=tk.BOTTOM, pady=10)

        self.master.mainloop()

    @staticmethod
    def paypal():
        webbrowser.open_new("https://www.paypal.com/cgi-bin/webscr?"
            "cmd=_s-xclick&hosted_button_id=986PSAHLH6N4L")

#-------------------------------------------------------------------------
# clase: Game(Base)
#-------------------------------------------------------------------------
class Game(Base):

    def __init__(self, master):
        super().__init__(master)
        self.master = master

        self.ahorcado = Juego()
        # Comprueba que se ha obtenido palabra online
        if self.datos.nivel != "Temas" and self.ahorcado.palabra == "":
            msg = ("Por problemas de conexión el juego ha cambiado al nivel "
                "«Temas».\nPuedes seguir jugando en este nivel o intentar otra "
                "vez un modo\nonline como «Avanzado» o «Júnior».\n\n"
                "Comprueba el estado de tu conexión a internet si este mensaje "
                "se\nmuestra de nuevo.")
            winErrorNet = tk.Toplevel(self.master)
            winErrorNet.resizable(0,0)
            pX = self.datos.posicion_x
            pY = self.datos.posicion_y
            winErrorNet.geometry("+{}+{}".format(pX, pY))

            tk.Label(winErrorNet, text=msg, justify="left").pack(anchor="center",
                padx=10,pady=20)
            boton = ttk.Button(winErrorNet, text='Cerrar', command=winErrorNet.destroy)
            boton.bind('<Return>', lambda e: winErrorNet.destroy())
            boton.focus()
            boton.pack(side=tk.BOTTOM, padx=20, pady=20)
            winErrorNet.focus_set()
            winErrorNet.grab_set()
            winErrorNet.transient(self.master)
            self.master.wait_window(winErrorNet)
            super().cambiar_nivel(self.niveles, "Temas") # self.cambiar_clase(Game)
            self.ahorcado = Juego()

        self.pista_horca()
        self.letra_oculta()
        self.teclado()
        self.master.mainloop()

    def pista_horca(self):  # Contenedor Pista + Horca
        contenedor = tk.Frame(self.master, background="#121")
        contenedor.pack(side=tk.TOP, anchor="n", expand=False, ipady=10)
        # Pista para Temas
        canvasPista = tk.Canvas(contenedor, width=32, height=32,
            background="#121", bd=0, highlightthickness=0)
        canvasPista.pack(side=tk.TOP, anchor="ne", expand=False, pady=4)
        if self.datos.nivel == "Temas":
            try:
                self.filePista = tk.PhotoImage(file=files["pista"])
            except:
                print("ERROR: ARCHIVO NO ENCONTRADO.")
                self.filePista = tk.PhotoImage()
            canvasPista.create_image(0, 0, anchor="nw", image=self.filePista)
            canvasPista.bind("<Button-1>",
                lambda e: tk.messagebox.showinfo("Pista", self.ahorcado.pista))
        # Horca
        self.canvasHorca = tk.Canvas(contenedor, width=403, height=435,
            background="#121", bd=0, highlightthickness=0)
        self.canvasHorca.pack(side=tk.TOP, anchor="n", expand=False, padx=30)
        self.imgFile = []
        for i in range(1, 8):
            fuente = "resources/img/"+str(i)+".png"
            fileFuente=os.path.join(os.path.dirname(__file__), fuente)
            try:
                self.imgFile.append(tk.PhotoImage(file=fileFuente))
            except:
                print("ERROR: ARCHIVO NO ENCONTRADO.")
                self.imgFile.append(tk.PhotoImage())
        self.imgHorca = self.canvasHorca.create_image(0, 0, anchor="nw",
            image=self.imgFile[0])

    def letra_oculta(self):  # Letra oculta
        self.var = tk.StringVar()
        palabaSecreta = tk.Label(self.master, textvariable = self.var,
            fg="white", bg="#121", font=("Courier", 32, "bold"))
        palabaSecreta.pack(anchor="s", pady=0, ipady=4)
        self.var.set(" ".join(self.ahorcado.secreta))

    def teclado(self):  # Teclado
        letrasFila = ["ABCDEFGHI", "JKLMNÑOPQ", "RSTUVWXYZ"]
        self.teclado = tk.Frame(self.master)
        for fila in letrasFila:
            self.keyboard(fila)
        self.teclado.pack(pady=0, anchor="n")

    def keyboard(self, letrasFila):
        fila = tk.Frame(self.teclado)
        teclas = list(letrasFila)
        for letra in teclas:
            nameBtn = ttk.Button(fila, text=letra, style='key.TButton', width=3)
            nameBtn["command"] = (lambda arg1=letra, arg2=nameBtn:
                self.letraPulsada(arg1, arg2))
            nameBtn.pack(side=tk.LEFT, ipady=4)
        fila.pack()

    def sonido_efecto(self, efecto):
        if self.datos.sonido:  # == True:  # is True:
            if sys.platform.startswith('linux'):
                threading.Thread(target=lambda: call(
                    ["aplay", files[efecto]])).start()

    def letraPulsada(self, let, btn):
        victoria = False
        self.errores = 0
        btn.config(state = tk.DISABLED)
        if let not in self.ahorcado.palabra:
            self.errores = self.ahorcado.sumaError()
            threading.Thread(target=lambda: self.canvasHorca.itemconfig(
                self.imgHorca, image=self.imgFile[self.errores])).start()
            if self.errores < 6:
                self.sonido_efecto("error")
            elif self.errores == 6:
                self.sonido_efecto("gameover")
                self.datos.guardar_marcador(d=1)
                otra = tk.messagebox.askokcancel("AHORCADO",
                    "Has perdido. La palabra era {}\n\n¿Otra partida?".format(
                    self.ahorcado.palabra))
        else:
            check = self.ahorcado.checkLetra(let)
            self.var.set(" ".join(check))
            victoria = self.ahorcado.checkVictoria(check)
            if not victoria:  # victoria == False:
                self.sonido_efecto("acierto")
            else:
                self.sonido_efecto("victoria")
                self.datos.guardar_marcador(v=1)
                otra = tk.messagebox.askokcancel("VICTORIA",
                    "Felicidades, has ganado\n\n¿Otra partida?")
        if self.errores == 6 or victoria == True:
            self.cambiar_clase(Game) if otra else self.cambiar_clase(StartPage)

#-------------------------------------------------------------------------
# clase: Marcador(Base)
#-------------------------------------------------------------------------
class Marcador(Base):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        try:
            imgM = tk.PhotoImage(file=files["marcador"])
        except:
            print("ERROR: ARCHIVO NO ENCONTRADO.")
            imgM = tk.PhotoImage()
        canvasM = tk.Canvas(self.master, width=435, height=48,
            background="#121", bd=0, highlightthickness=0)
        canvasM.create_image(0, 0, anchor="nw", image=imgM)
        canvasM.pack(side=tk.TOP, expand=False, padx=30, pady=60)

        frameTrofeos = tk.Frame(self.master, bg="#121")

        frameV = tk.Frame(frameTrofeos, bg="#121")
        try:
            trofeo = tk.PhotoImage(file=files["triunfos"])
        except:
            print("ERROR: ARCHIVO NO ENCONTRADO.")
            trofeo = tk.PhotoImage()
        canvasTrofeo = tk.Canvas(frameV, width=64, height=64,
            background="#121", bd=0, highlightthickness=0)
        canvasTrofeo.create_image(0, 0, anchor="nw", image=trofeo)
        canvasTrofeo.pack(side=tk.TOP, expand=False, padx=30)
        self.tanV = tk.StringVar()
        puntVictorias = tk.Label(frameV, textvariable = self.tanV,
            fg="white", bg="#121", font=("Courier", 32, "bold"))
        self.tanV.set(self.datos.victorias)
        puntVictorias.pack(side=tk.TOP, expand=False, padx=30, pady=20)
        frameV.pack(side=tk.LEFT)

        frameD = tk.Frame(frameTrofeos, bg="#121")
        try:
            soga = tk.PhotoImage(file=files["derrotas"])
        except:
            print("ERROR: ARCHIVO NO ENCONTRADO.")
            soga = tk.PhotoImage()
        canvasSoga = tk.Canvas(frameD, width=64, height=64,
            background="#121", bd=0, highlightthickness=0)
        canvasSoga.create_image(0, 0, anchor="nw", image=soga)
        canvasSoga.pack(side=tk.TOP, expand=False, padx=30)
        self.tanD = tk.StringVar()
        puntDerrotas = tk.Label(frameD, textvariable = self.tanD,
            fg="white", bg="#121", font=("Courier", 32, "bold"))
        self.tanD.set(self.datos.derrotas)
        puntDerrotas.pack(side=tk.TOP, expand=False, padx=30, pady=20)
        frameD.pack(side=tk.LEFT)

        frameTrofeos.pack(side=tk.TOP, expand=False, pady=2)

        frameBtn = tk.Frame(self.master, bg="#121")
        ttk.Button(frameBtn, text="Reset", width=10, style="gran.TButton",
            command=self.resetear).pack(side=tk.LEFT, ipady=8)
        ttk.Button(frameBtn, text="Inicio", width=10, style="gran.TButton",
            command=lambda: self.cambiar_clase(StartPage)).pack(side=tk.LEFT, ipady=8)
        ttk.Button(frameBtn, text="Jugar", width=10, style="gran.TButton",
            command=lambda: self.cambiar_clase(Game)).pack(side=tk.LEFT, ipady=8)
        frameBtn.pack(side=tk.BOTTOM, expand=False, padx=30, pady=20)

        self.master.mainloop()

    def resetear(self):
        self.datos.reset_marcador()
        self.tanV.set(self.datos.victorias)
        self.tanD.set(self.datos.derrotas)

def main():
    msg=("""
        El juego arrancará enseguida,
        estamos recuperando datos y...
            preparando la horca.""")
    Popup(msg, tit="inicio")

    root = tk.Tk()
    winAncho = root.winfo_reqwidth()  # root.winfo_width()
    winAlto = root.winfo_reqheight()  # root.winfo_height()
    posX = str(int(root.winfo_screenwidth()/3 - winAncho/2))
    posY = str(int(root.winfo_screenheight()/4 - winAlto/2))
    root.geometry("700x700+{}+{}".format(posX, posY))
    StartPage(root)
    root.mainloop()

if __name__ == "__main__":
    main()

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

from ahorcado.juego import Juego  #import ahorcado.juego
from ahorcado.datos import Datos  #import ahorcado.datos

#-------------------------------------------------------------------------
# clase: Checkbar(tk.Frame)#
#-------------------------------------------------------------------------
class Checkbar(tk.Frame):

    def __init__(self, win, dick):
        tk.Frame.__init__(self, win)
        frameIz = tk.Frame(self)
        frameDr = tk.Frame(self)
        frameID = frameIz
        self.cbuts = []
        self.catego = []
        self.vars = []
        for ele in dick:
            var = tk.BooleanVar()
            if dick[ele] == True:
                var.set(True)
            chk = tk.Checkbutton(frameID, text=ele.upper(), variable=var, command=self.no_all)
            chk.pack(side=tk.TOP, anchor="w", expand="no", padx=20)
            self.vars.append(var)
            self.catego.append(ele)
            if frameID == frameIz:
                frameID = frameDr
            else:
                frameID = frameIz
            self.cbuts.append(chk)
        self.varT = tk.BooleanVar()
        self.chkT = tk.Checkbutton(frameDr, text="TODO", variable=self.varT,
            command=self.select_all)
        self.chkT.pack(side=tk.TOP, anchor="w", expand="no", padx=20)
        frameIz.pack(side=tk.LEFT, expand="yes")
        frameDr.pack(side=tk.LEFT, expand="yes")

    def no_all(self):
        self.chkT.deselect()  # self.varT.set(False)

    def select_all(self):
        for chk in self.cbuts:
            chk.select()  # chk.invoke()

    def check_temas(self, dictConfirmado):
        for tema in dictConfirmado:
            if dictConfirmado[tema] == True:
                return True
        return False

    def state(self):
        valores = list(map((lambda var: var.get()), self.vars))
        newDict = dict(zip(self.catego, valores))
        selectOk = self.check_temas(newDict)
        if selectOk == True:
            return newDict
        else:
            return False

#-------------------------------------------------------------------------
# clase: Base()
#-------------------------------------------------------------------------
class Base:

    def __init__(self, master):
        self.ahorcado = Juego()  # ahorcado = ahorcado.juego.Juego()
        self.datos = Datos()     # datos = ahorcado.datos.Datos()

        # Fuentes y estilos
        font.nametofont("TkDefaultFont").configure(family="Helvetica", size=12)
        font.nametofont("TkMenuFont").configure(family="Helvetica", size=11)
        font.nametofont("TkCaptionFont").configure(family="Helvetica", size=12,
            weight="normal")
        ttk.Style().configure('gran.TButton', font=("Helvetica", 18))
        ttk.Style().configure('key.TButton', font=("Helvetica", 16))

        # Ventana
        self.master = master
        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.master.title("El Ahorcado")
        winAncho = self.master.winfo_reqwidth()
        winAlto = self.master.winfo_reqheight()
        posDcha = int(self.master.winfo_screenwidth()/3 - winAncho/2)
        posBajo = int(self.master.winfo_screenheight()/4 - winAlto/2)
        self.master.geometry("600x700+{}+{}".format(posDcha, posBajo))
        self.master.configure(background="#121")

        # Menu
        self.menuApp = tk.Menu(self.master)
        self.master.config(menu=self.menuApp)
        self.opcGame = tk.Menu(self.menuApp, tearoff=0)
        self.opcInfo = tk.Menu(self.menuApp, tearoff=0)
        self.menuApp.add_cascade(menu=self.opcGame, label="Juego")
        self.menuApp.add_cascade(menu=self.opcInfo, label="Info")

        self.opcGame.add_command(label="Nuevo Juego", underline=0,
            command=lambda: self.cambiar_clase(Game), accelerator="Alt+N")
        self.opcGame.add_command(label="Marcador",
            command=lambda: self.cambiar_clase(Marcador))
        self.opcGame.add_separator()

        self.opcGame.add_command(label="Temas",
            command=self.temas)

        if self.datos.sonido == True:
            self.opcGame.add_command(label="Sonido: OK",
                command=lambda: self.cambiar_sonido(self.opcGame))
        else:
            self.opcGame.add_command(label="Sonido: Mute",
                command=lambda: self.cambiar_sonido(self.opcGame))
        self.opcGame.add_separator()
        self.opcGame.add_command(label="Salir",
            command=quit, accelerator="Alt+Q")
        self.master.bind_all("<Alt-n>", lambda event: self.cambiar_clase(Game))
        self.master.bind_all("<Alt-q>", lambda event: quit())

        self.opcInfo.add_command(label="Ayuda",
            command=lambda:self.info(os.path.join(os.path.dirname(__file__),
            "resources/txt/HELP.rst")))
        self.opcInfo.add_command(label="Acerca de",
            command=lambda:self.info(os.path.join(os.path.dirname(__file__),
            "resources/txt/ABOUT.rst")))

    def on_closing(self):
        sys.exit()  #self.salir()

    def info(self, archivoInfo):
        self.dialogo = tk.Toplevel(self.master)
        self.dialogo.resizable(0,0)
        sw = self.dialogo.winfo_screenwidth()  # posicion
        sh = self.dialogo.winfo_screenheight()
        sd = (sw - sh)
        self.dialogo.geometry("600x600+%d+%d" %(sd/2, sd/6))

        frame_txt = tk.Frame(self.dialogo)
        text = tk.scrolledtext.ScrolledText(frame_txt,
            wrap="word", font=("Courier", 12))
        try:
            with open(archivoInfo, "r", encoding='utf-8') as archivoOpen:
                txtRead = archivoOpen.read()
        except:
            txtRead = "ERROR. ARCHIVO NO ENCONTRADO."
        text.insert(tk.END, txtRead)
        text.configure(state=tk.DISABLED, padx=10, pady=10)
        text.pack(fill=tk.BOTH, expand=1)
        frame_txt.pack(fill=tk.BOTH, expand=1, side=tk.TOP)

        boton = ttk.Button(self.dialogo, text='Cerrar',
            command=self.dialogo.destroy)
        boton.bind('<Return>', lambda e: self.dialogo.destroy())
        boton.focus()
        boton.pack(side=tk.BOTTOM, padx=20, pady=20)

        self.dialogo.focus_set()
        self.dialogo.grab_set()
        self.dialogo.transient(self.master)
        self.master.wait_window(self.dialogo)  #self.dialogo.mainloop()

    def cambiar_clase(self, clase):
        self.master.destroy()
        newRoot = tk.Tk()
        clase(newRoot)  # self.mainloop()

    def cambiar_sonido(self, menu):
        if self.datos.sonido == True:
            menu.entryconfigure(4, label="Sonido: Mute")
            self.datos.guardar_sonido(False)
        else:
            menu.entryconfigure(4, label="Sonido: OK")
            self.datos.guardar_sonido(True)

    def temas(self):
        self.winTemas = tk.Toplevel(self.master)
        self.winTemas.resizable(0,0)
        sw = self.winTemas.winfo_screenwidth()  # posicion
        sh = self.winTemas.winfo_screenheight()
        sd = (sw - sh)
        self.winTemas.geometry("600x600+%d+%d" %(sd/2, sd/6))
        self.winTemas.configure(background="#121")

        tk.Label(self.winTemas, text="Selecciona los temas del juego:", bg="#121",
            fg="white", bd=0).pack(pady=20)

        dictTemas = self.datos.return_temas()
        ditCheck = Checkbar(self.winTemas, dictTemas)
        ditCheck.pack(fill=tk.BOTH, expand="yes")
        ditCheck.config(relief=tk.GROOVE, bd=0)

        def allstates():
            newDictTemas = ditCheck.state()
            if newDictTemas:
                self.datos.guardar_temas(newDictTemas)
                self.cambiar_clase(Game)

        frameBtn = tk.Frame(self.winTemas, bg="#121")
        ttk.Button(frameBtn, text="Salir", width=10, style="gran.TButton",
            command=self.winTemas.destroy).pack(side=tk.LEFT, ipady=8)
        ttk.Button(frameBtn, text="Confirmar", width=10, style="gran.TButton",
            command=allstates).pack(side=tk.LEFT, ipady=8)
        frameBtn.pack(side=tk.BOTTOM, expand=False, padx=30, pady=20)

        self.winTemas.focus_set()
        self.winTemas.grab_set()
        self.winTemas.transient(self.master)
        self.master.wait_window(self.winTemas)
        self.winTemas.mainloop()

#-------------------------------------------------------------------------
# clase: StartPage(Base)
#-------------------------------------------------------------------------
class StartPage(Base):

    def __init__(self, master):
        super().__init__(master)
        self.master = master

        imgTitulo = tk.PhotoImage(file=os.path.join(os.path.dirname(__file__),
            "resources/img/ahorcado.png"))
        canvas = tk.Canvas(self.master, width=530, height=48,
            background="#121", bd=0, highlightthickness=0)
        canvas.create_image(0, 0, anchor="nw", image=imgTitulo)
        canvas.pack(side=tk.TOP, expand=False, padx=30, pady=30)

        imgIcon = tk.PhotoImage(file=os.path.join(os.path.dirname(__file__),
            "resources/img/icon128.png"))
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

        imgPaypal = tk.PhotoImage(file=os.path.join(os.path.dirname(__file__),
            "resources/img/donate.gif"))
        tk.Button(self.master, image=imgPaypal, cursor="hand1", bd=0,
            activebackground="#BDBDBD", command=self.paypal).pack(side=tk.BOTTOM,
            pady=10)

        self.master.mainloop()

    def paypal(self):
        webbrowser.open_new("https://www.paypal.com/cgi-bin/webscr?"
            "cmd=_s-xclick&hosted_button_id=986PSAHLH6N4L")

#-------------------------------------------------------------------------
# clase: Game(Base)
#-------------------------------------------------------------------------
class Game(Base):

    def __init__(self, master):
        super().__init__(master)
        self.master = master

        # Contenedor Pista + Horca
        contenedor = tk.Frame(self.master, background="#121")
        contenedor.pack(side=tk.TOP, anchor="n", expand=False, ipady=10)

        #Pista
        filePista = tk.PhotoImage(file=os.path.join(os.path.dirname(__file__),
            "resources/img/pista.png"))
        canvasPista = tk.Canvas(contenedor, width=32, height=32,
            background="#121", bd=0, highlightthickness=0)
        canvasPista.create_image(0, 0, anchor="nw", image=filePista)
        canvasPista.bind("<Button-1>", self.muestra_pista)
        canvasPista.pack(side=tk.TOP, anchor="ne", expand=False, pady=4)

        # Horca
        self.canvasHorca = tk.Canvas(contenedor, width=403, height=435,
            background="#121", bd=0, highlightthickness=0)
        self.canvasHorca.pack(side=tk.TOP, anchor="n", expand=False, padx=30)
        self.imgFile = []
        for i in range(1, 8):
            fuente = "resources/img/"+str(i)+".png"
            fileFuente=os.path.join(os.path.dirname(__file__), fuente)
            self.imgFile.append(tk.PhotoImage(file=fileFuente))
        self.imgHorca = self.canvasHorca.create_image(0, 0, anchor="nw",
            image=self.imgFile[0])

        # Letra oculta
        self.var = tk.StringVar()
        palabaSecreta = tk.Label(self.master, textvariable = self.var,
            fg="white", bg="#121", font=("Courier", 32, "bold"))
        palabaSecreta.pack(anchor="s", pady=0, ipady=4)
        self.var.set(" ".join(self.ahorcado.secreta))

        # Teclado
        letrasFila = ["ABCDEFGHI", "JKLMNÑOPQ", "RSTUVWXYZ"]
        self.teclado = tk.Frame(self.master)
        for fila in letrasFila:
            self.keyboard(fila)
        self.teclado.pack(pady=0, anchor="n")

        self.master.mainloop()

    def keyboard(self, letrasFila):
        fila = tk.Frame(self.teclado)
        teclas = list(letrasFila)
        for letra in teclas:
            nameBtn = ttk.Button(fila, text=letra, style='key.TButton',
                width=3)
            nameBtn["command"] = (lambda arg1=letra, arg2=nameBtn :
                self.letraPulsada(arg1, arg2))
            nameBtn.pack(side=tk.LEFT, ipady=4)
        fila.pack()

    def dibujaError(self):
        self.canvasHorca.itemconfig(self.imgHorca, image=self.imgFile[self.errores])

    def sonidoEfecto(self, file):
        if self.datos.sonido == True:
            if sys.platform.startswith('linux'):
                call(["aplay", file])  #os.system("aplay {}".format(file))

    def letraPulsada(self, let, btn):
        fileSonidos = {
            "Error": os.path.join(os.path.dirname(__file__),
                "resources/media/error.wav"),
            "Acierto": os.path.join(os.path.dirname(__file__),
                "resources/media/acierto.wav"),
            "Gameover": os.path.join(os.path.dirname(__file__),
                "resources/media/gameover.wav"),
            "Victoria": os.path.join(os.path.dirname(__file__),
                "resources/media/victoria.wav")}
        victoria = False
        self.errores = 0
        btn.config(state = tk.DISABLED)
        check = self.ahorcado.checkLetra(let)
        if check == False:
            self.errores = self.ahorcado.sumaError()
            hiloDibujo = threading.Thread(target=self.dibujaError)
            if self.errores < 6:
                hiloSonido = threading.Thread(target=self.sonidoEfecto,
                    args=(fileSonidos["Error"],))
                hiloSonido.start()
                hiloDibujo.start()
            elif self.errores == 6:
                hiloSonido = threading.Thread(target=self.sonidoEfecto,
                    args=(fileSonidos["Gameover"],))
                hiloSonido.start()
                hiloDibujo.start()
                self.datos.guardar_marcador(d=1)
                otra = self.ventanaFin("AHORCADO",
                    "Has perdido. La palabra era {}\n\n¿Otra partida?".format(
                    self.ahorcado.palabra))
        else:
            self.var.set(" ".join(check))
            victoria = self.ahorcado.checkVictoria(check)
            if victoria == False:
                hiloSonido = threading.Thread(target=self.sonidoEfecto,
                    args=(fileSonidos["Acierto"],))
                hiloSonido.start()
            else:
                hiloSonido = threading.Thread(target=self.sonidoEfecto,
                    args=(fileSonidos["Victoria"],))
                hiloSonido.start()
                self.datos.guardar_marcador(v=1)
                otra = self.ventanaFin("VICTORIA",
                    "Felicidades, has ganado\n\n¿Otra partida?")
        if self.errores == 6 or victoria == True:
            if otra == True:
                self.cambiar_clase(Game)
            else:
                self.cambiar_clase(StartPage)

    def ventanaFin(self, tit, msg):
        return tk.messagebox.askokcancel(tit, msg)

    def muestra_pista(self, event):
        tk.messagebox.showinfo("Pista", self.ahorcado.pista)

#-------------------------------------------------------------------------
# clase: Marcador(Base)
#-------------------------------------------------------------------------
class Marcador(Base):
    def __init__(self, master):

        super().__init__(master)
        self.master = master

        imgM = tk.PhotoImage(file=os.path.join(os.path.dirname(__file__),
            "resources/img/marcador.png"))
        canvasM = tk.Canvas(self.master, width=435, height=48,
            background="#121", bd=0, highlightthickness=0)
        canvasM.create_image(0, 0, anchor="nw", image=imgM)
        canvasM.pack(side=tk.TOP, expand=False, padx=30, pady=60)

        frameTrofeos = tk.Frame(self.master, bg="#121")

        frameV = tk.Frame(frameTrofeos, bg="#121")
        trofeo = tk.PhotoImage(file=os.path.join(os.path.dirname(__file__),
            "resources/img/triunfos.png"))
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
        soga = tk.PhotoImage(file=os.path.join(os.path.dirname(__file__),
            "resources/img/derrotas.png"))
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
    root = tk.Tk()
    StartPage(root)

if __name__ == "__main__":
    main()

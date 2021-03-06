import sys
import webbrowser
import threading
from random import choice
try:
    import tkinter as tk
    import tkinter.font as font
    from tkinter import ttk
    from tkinter import scrolledtext
    from tkinter import messagebox
except ImportError:
    print("Se requiere el modulo tkinter. Más información en about.txt")
    sys.exit(1)

from ahorcado.dialogo import Dialogo
try:
    import simpleaudio as sa
except ImportError:
    msgError = (
        "Los efectos de sonido requieren el\nmódulo simpleaudio (no encontrado)."
        "\n\nEl sonido ha sido desactivado, aunque\nel juego es plenamente funcional.")
    Dialogo(error=msgError)
    audio = False
else:
    audio = True

from ahorcado import VERSION
from ahorcado.juego import Juego
from ahorcado.datos import Datos
from ahorcado.pop import Popup
from ahorcado.archivos import files
from ahorcado.archivos import filesHorca

#-------------------------------------------------------------------------
# clase: Base()
#-------------------------------------------------------------------------
class Base(object):

    modos = {"Avanzado": 0, "Júnior": 1, "Temas": 2}

    def __init__(self, master):

        self.datos = Datos()
        try:
            self.startpage, self.game, self.marcador = [cls for cls in Base.__subclasses__()]
        except ValueError as e:
            Dialogo(master, error=e)
        except Exception as e:
            Dialogo(master, error=e)

        # Fuentes y estilos
        fuentes = ["TkDefaultFont", "TkMenuFont", "TkCaptionFont"]
        for f in fuentes:
            font.nametofont(f).configure(family="Helvetica", size=12, weight="normal")
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
        self.menuGame = tk.Menu(
            self.menuApp, tearoff=0, bd=2, activeborderwidth=2, relief=tk.GROOVE)
        self.menuEdit = tk.Menu(
            self.menuApp, tearoff=0, bd=2, activeborderwidth=2, relief=tk.GROOVE)
        self.menuInfo = tk.Menu(
            self.menuApp, tearoff=0, bd=2, activeborderwidth=2, relief=tk.GROOVE)
        self.menuApp.add_cascade(menu=self.menuGame, label="Juego")
        self.menuApp.add_cascade(menu=self.menuEdit, label="Editar")
        self.menuApp.add_cascade(menu=self.menuInfo, label="Info")

        self.menuGame.add_command(
            label="Nuevo Juego", underline=0,
            command=lambda: self.cambiar_clase(self.game), accelerator="Alt+N")
        self.menuGame.add_command(
            label="Marcador", command=lambda: self.cambiar_clase(self.marcador))
        self.menuGame.add_separator()
        self.menuGame.add_command(
            label="Salir", command=sys.exit, accelerator="Alt+Q")
        self.master.bind_all("<Alt-n>", lambda event: self.cambiar_clase(self.game))
        self.master.bind_all("<Alt-q>", lambda event: sys.exit())

        self.niveles = tk.Menu(
            self.menuEdit, tearoff=0, bd=2, activeborderwidth=2, relief=tk.GROOVE)
        self.menuEdit.add_cascade(menu=self.niveles, label="Nivel ")
        for clave in self.modos:
            self.niveles.add_command(
                label=clave,
                command=lambda arg=clave: self.cambiar_nivel(self.niveles, arg))
        self.niveles.entryconfigure(self.modos[self.datos.nivel], state="disabled")

        self.sonido = tk.Menu(
            self.menuEdit, tearoff=0, bd=2, activeborderwidth=2, relief=tk.GROOVE)
        self.menuEdit.add_cascade(menu=self.sonido, label="Sonido ")
        self.sonido.add_command(
            label="OK", command=lambda: self.cambiar_sonido(self.sonido, True))
        self.sonido.add_command(
            label="Mute", command=lambda: self.cambiar_sonido(self.sonido, False))
        if audio:
            entry = 0 if self.datos.sonido else 1
        else:
            self.cambiar_sonido(self.sonido, False)
            entry = 0
        self.sonido.entryconfigure(entry, state="disabled")

        self.menuInfo.add_command(
            label="Ayuda", command=lambda: self.info(files.get("help", "ERROR")))
        self.menuInfo.add_command(
            label="Acerca de", command=lambda: self.info(files.get("about", "ERROR")))

    def get_geometry(self, win, ancho, alto):
        win_width = self.master.winfo_width()
        win_height = self.master.winfo_height()
        win_x = self.master.winfo_x()
        win_y = self.master.winfo_y()
        x = win_x + ((win_width // 2) - (ancho // 2))
        y = win_y + ((win_height // 2) - (alto // 2))
        win.geometry('{}x{}+{}+{}'.format(ancho, alto, x, y))

    def info(self, archivoInfo):
        dialogo = tk.Toplevel(self.master)
        dialogo.title("El Ahorcado " + VERSION)
        dialogo.resizable(0,0)
        self.get_geometry(dialogo, 600, 600)

        frame_txt = tk.Frame(dialogo)
        text = tk.scrolledtext.ScrolledText(
            frame_txt, wrap="word", font=("Courier", 12))
        try:
            with open(archivoInfo, "r", encoding='utf-8') as archivoOpen:
                txtRead = archivoOpen.read()
        except Exception:
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
        if clase:
            for widget in self.master.winfo_children():
                widget.destroy()
            clase(self.master)
        else:
            Dialogo(self.master, error="Transición de ventanas")

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

        imgTitulo = tk.PhotoImage(file=files.get("titulo", "")) # try?
        canvas = tk.Canvas(
            self.master, width=530, height=48,background="#121", bd=0, highlightthickness=0)
        canvas.create_image(0, 0, anchor="nw", image=imgTitulo)
        canvas.pack(side=tk.TOP, expand=False, padx=30, pady=30)

        imgIcon = tk.PhotoImage(file=files.get("icono", ""))
        canvasIcon = tk.Canvas(
            self.master, width=128, height=128, background="#121", bd=0, highlightthickness=0)
        canvasIcon.create_image(0, 0, anchor="nw", image=imgIcon)
        canvasIcon.pack(side=tk.TOP, expand=False, padx=30, pady=10)

        btnGame = ttk.Button(
            self.master, text="Nuevo Juego", style="gran.TButton", width=25,
            command=lambda: self.cambiar_clase(self.game))
        btnPunt = ttk.Button(
            self.master, text="Marcador", style="gran.TButton", width=25,
            command=lambda: self.cambiar_clase(self.marcador))
        btnGame.pack(side=tk.TOP, fill=tk.BOTH, padx=30, pady=10, ipady=10)
        btnPunt.pack(side=tk.TOP, fill=tk.BOTH, padx=30, pady=0, ipady=10)

        imgPaypal = tk.PhotoImage(file=files.get("paypal", ""))
        tk.Button(
            self.master, image=imgPaypal, cursor="hand1", bd=0, highlightthickness=0,
            background="#121", activebackground="#121", command=self.paypal).pack(
                side=tk.BOTTOM, pady=10)

        self.master.mainloop()

    @staticmethod
    def paypal():
        webbrowser.open_new_tab(
            ("https://www.paypal.com/cgi-bin/webscr?"
            "cmd=_s-xclick&hosted_button_id=986PSAHLH6N4L")
        )

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
            msg = (
                "Por problemas de conexión el juego ha cambiado al nivel "
                "«Temas».\nPuedes seguir jugando en este nivel o intentar otra "
                "vez un modo\nonline como «Avanzado» o «Júnior».\n\n"
                "Comprueba el estado de tu conexión a internet si este mensaje "
                "se\nmuestra de nuevo.")
            winErrorNet = tk.Toplevel(self.master)
            self.get_geometry(winErrorNet, 600, 200)

            tk.Label(winErrorNet, text=msg, justify="left").pack(
                anchor="center", padx=10, pady=10)
            boton = ttk.Button(winErrorNet, text='Cerrar', command=winErrorNet.destroy)
            boton.bind('<Return>', lambda e: winErrorNet.destroy())
            boton.focus()
            boton.pack(side=tk.BOTTOM, padx=20, pady=10)
            winErrorNet.focus_set()
            winErrorNet.grab_set()
            winErrorNet.transient(self.master)
            self.master.wait_window(winErrorNet)
            self.cambiar_nivel(self.niveles, "Temas")  # super()
            self.ahorcado = Juego()

        self.pista_horca()
        self.letra_oculta()  # self.teclado()
        self.master.mainloop()

    def muestra_pista(self):
        self.filePista = tk.PhotoImage(file=files.get("pista", ""))
        self.canvasPista.create_image(0, 0, anchor="nw", image=self.filePista)
        self.canvasPista.bind(
            "<Button-1>", lambda e: tk.messagebox.showinfo("Pista", self.ahorcado.pista))

    def pista_horca(self):
        self.contenedor = tk.Frame(self.master, background="#121")
        self.contenedor.pack(side=tk.TOP, anchor="n", expand=False, ipady=10)

        self.canvasPista = tk.Canvas(
            self.contenedor, width=32, height=32, background="#121", bd=0, highlightthickness=0)
        self.canvasPista.pack(side=tk.TOP, anchor="ne", expand=False, pady=4)

        self.canvasHorca = tk.Canvas(
            self.contenedor, width=403, height=435, background="#121", bd=0, highlightthickness=0)
        self.canvasHorca.pack(side=tk.TOP, anchor="n", expand=False, padx=30)
        self.imgFile = [tk.PhotoImage(file=archivo) for archivo in filesHorca]
        self.imgHorca = self.canvasHorca.create_image(
            0, 0, anchor="nw", image=self.imgFile[0])

    def update_label(self, lbl, var):
        if self.count < 10:
            letras = (
                "________________________________"
                "AAAABCDEEEEFGHIIIIJKLMNÑOOOOPQRSTUUUUVWXYZ")
            palabra = ""
            self.sonido_efecto(files.get("tecla", ""))
            for x in range(7):
                letra = choice(letras)
                palabra = palabra + " " + letra
            var.set(palabra)
            lbl.after(100, lambda: self.update_label(lbl, var))
            self.count += 1
        else:
            self.var.set(" ".join(self.ahorcado.secreta))
            if self.datos.nivel == "Temas":
                self.muestra_pista()
            self.teclado()

    def letra_oculta(self):
        self.var = tk.StringVar()
        palabaSecreta = tk.Label(
            self.master, textvariable = self.var, fg="white", bg="#121",
            font=("Courier", 32, "bold"))
        palabaSecreta.pack(anchor="s", pady=0, ipady=4)
        self.count = 0
        self.update_label(palabaSecreta, self.var)

    def teclado(self):
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
            nameBtn["command"] = (
                lambda arg1=letra, arg2=nameBtn: self.letraPulsada(arg1, arg2))
            nameBtn.pack(side=tk.LEFT, ipady=4)
        fila.pack()

    def letraPulsada(self, let, btn):
        victoria = False
        self.errores = 0
        btn.config(state = tk.DISABLED)
        if let not in self.ahorcado.palabra:
            self.errores = self.ahorcado.sumaError()
            threading.Thread(target=lambda: self.canvasHorca.itemconfig(
                self.imgHorca, image=self.imgFile[self.errores])).start()
            if self.errores < 6:
                self.sonido_efecto(files.get("error", ""))
            elif self.errores == 6:
                self.sonido_efecto(files.get("gameover", ""))
                self.datos.guardar_marcador(d=1)
                otra = tk.messagebox.askokcancel(
                    "AHORCADO",
                    ("Has perdido. La palabra era {}\n\n¿Otra partida?").format(
                        self.ahorcado.palabra))
        else:
            check = self.ahorcado.checkLetra(let)
            self.var.set(" ".join(check))
            victoria = self.ahorcado.checkVictoria(check)
            if not victoria:
                self.sonido_efecto(files.get("acierto", ""))
            else:
                self.sonido_efecto(files.get("victoria", ""))
                self.datos.guardar_marcador(v=1)
                otra = tk.messagebox.askokcancel(
                    "VICTORIA", "Felicidades, has ganado\n\n¿Otra partida?")
        if self.errores == 6 or victoria == True:
            if otra:
                self.cambiar_clase(self.game)  # super().cambiar_clase(Game)
            else:
                self.cambiar_clase(self.startpage)

    def sonido_efecto(self, efecto):
        def inicio_sonido():
            try:
                wave_obj = sa.WaveObject.from_wave_file(efecto)
            except FileNotFoundError as e:
                print("ERROR. ARCHIVO DE SONIDO NO ENCONTRADO.")
            except Exception:
                print("ERROR. ARCHIVO DE SONIDO NO ENCONTRADO.")
            else:
                play_obj = wave_obj.play()
                play_obj.wait_done()
        if self.datos.sonido:
            if efecto:
                threading.Thread(target=lambda: inicio_sonido()).start()

#-------------------------------------------------------------------------
# clase: Marcador(Base)
#-------------------------------------------------------------------------
class Marcador(Base):

    def __init__(self, master):
        super().__init__(master)
        self.master = master

        imgM = tk.PhotoImage(file=files.get("marcador", ""))
        canvasM = tk.Canvas(
            self.master, width=435, height=48, background="#121", bd=0, highlightthickness=0)
        canvasM.create_image(0, 0, anchor="nw", image=imgM)
        canvasM.pack(side=tk.TOP, expand=False, padx=30, pady=60)

        frameTrofeos = tk.Frame(self.master, bg="#121")

        frameV = tk.Frame(frameTrofeos, bg="#121")
        trofeo = tk.PhotoImage(file=files.get("triunfos", ""))
        canvasTrofeo = tk.Canvas(
            frameV, width=64, height=64, background="#121", bd=0, highlightthickness=0)
        canvasTrofeo.create_image(0, 0, anchor="nw", image=trofeo)
        canvasTrofeo.pack(side=tk.TOP, expand=False, padx=30)
        self.tanV = tk.StringVar()
        puntVictorias = tk.Label(
            frameV, textvariable = self.tanV, fg="white", bg="#121",
            font=("Courier", 32, "bold"))
        self.tanV.set(self.datos.victorias)
        puntVictorias.pack(side=tk.TOP, expand=False, padx=30, pady=20)
        frameV.pack(side=tk.LEFT)

        frameD = tk.Frame(frameTrofeos, bg="#121")
        soga = tk.PhotoImage(file=files.get("derrotas", ""))
        canvasSoga = tk.Canvas(
            frameD, width=64, height=64, background="#121", bd=0, highlightthickness=0)
        canvasSoga.create_image(0, 0, anchor="nw", image=soga)
        canvasSoga.pack(side=tk.TOP, expand=False, padx=30)
        self.tanD = tk.StringVar()
        puntDerrotas = tk.Label(
            frameD, textvariable = self.tanD, fg="white", bg="#121",
            font=("Courier", 32, "bold"))
        self.tanD.set(self.datos.derrotas)
        puntDerrotas.pack(side=tk.TOP, expand=False, padx=30, pady=20)
        frameD.pack(side=tk.LEFT)

        frameTrofeos.pack(side=tk.TOP, expand=False, pady=2)

        frameBtn = tk.Frame(self.master, bg="#121")
        ttk.Button(
            frameBtn, text="Reset", width=10, style="gran.TButton",
            command=self.resetear).pack(side=tk.LEFT, ipady=8)
        ttk.Button(
            frameBtn, text="Inicio", width=10, style="gran.TButton",
            command=lambda: self.cambiar_clase(self.startpage)).pack(
                side=tk.LEFT, ipady=8)
        ttk.Button(
            frameBtn, text="Jugar", width=10, style="gran.TButton",
            command=lambda: self.cambiar_clase(self.game)).pack(
                side=tk.LEFT, ipady=8)
        frameBtn.pack(side=tk.BOTTOM, expand=False, padx=30, pady=20)

        self.master.mainloop()

    def resetear(self):
        self.datos.reset_marcador()
        self.tanV.set(self.datos.victorias)
        self.tanD.set(self.datos.derrotas)

#-------------------------------------------------------------------------
# RUN RUN
#-------------------------------------------------------------------------
def main():

    def create_win(clase, ancho, alto):
        win = tk.Tk()
        x = (win.winfo_screenwidth() // 2) - (ancho // 2)
        y = (win.winfo_screenheight() // 2) - (alto // 2)
        win.geometry('{}x{}+{}+{}'.format(ancho, alto, x, y))
        clase(win)
        win.mainloop()

    create_win(Popup, 400, 300)
    create_win(StartPage, 700, 700)

if __name__ == "__main__":
    main()

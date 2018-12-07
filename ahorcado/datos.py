import configparser
from ahorcado.palabras import Vocabulario

#-------------------------------------------------------------------------
# clase: Datos()
#-------------------------------------------------------------------------
class Datos:

    def __init__(self):
        self.configuracion = configparser.ConfigParser()
        self.configuracion["Marcador"] = {
            "victorias": "0", "derrotas": "0"}
        self.configuracion["General"] = {"sonido": "True"}
        self.configuracion["Temas"] = {}

        self.vocabulario = Vocabulario()
        categoriasLista = self.vocabulario.all_categorias()
        for nombreTema in categoriasLista:
            self.configuracion["Temas"][nombreTema] = "True"

        try:
            self.configuracion.read("config.cfg")
        except:
            with open("config.cfg", "w") as archivoconfig:
                self.configuracion.write(archivoconfig)

        self.victorias = int(self.configuracion["Marcador"].get("victorias"))
        self.derrotas = int(self.configuracion["Marcador"].get("derrotas"))

        self.sonido = self.configuracion.getboolean("General", "sonido")

        self.temas = {}
        for cat, valor in self.configuracion["Temas"].items():
            self.temas[cat] = self.configuracion.getboolean("Temas", cat)
            self.cat = self.configuracion.getboolean("Temas", cat)

    def guardar_marcador(self, v=0, d=0):
        if v == 1:
            self.victorias += 1
        if d == 1:
            self.derrotas += 1
        self.configuracion.set("Marcador", "victorias", str(self.victorias))
        self.configuracion.set("Marcador", "derrotas", str(self.derrotas))
        with open("config.cfg", "w") as archivoconfig:
            self.configuracion.write(archivoconfig)

    def reset_marcador(self):
        self.victorias = 0
        self.derrotas = 0
        self.configuracion.set("Marcador", "victorias", str(self.victorias))
        self.configuracion.set("Marcador", "derrotas", str(self.derrotas))
        with open("config.cfg", "w") as archivoconfig:
            self.configuracion.write(archivoconfig)

    def guardar_sonido(self, sond):
        self.sonido = sond
        self.configuracion.set("General", "sonido", str(self.sonido))
        with open("config.cfg", "w") as archivoconfig:
            self.configuracion.write(archivoconfig)

    def guardar_temas(self, dictTemas):
        self.temas = {}
        for tema, valor in dictTemas.items():
            self.temas[tema] = str(valor)  # self.temas[tema] = str(valor.get())
            self.tema = str(valor)
            self.configuracion.set("Temas", tema, str(self.tema))
        with open("config.cfg", "w") as archivoconfig:
            self.configuracion.write(archivoconfig)

    def return_temas(self):
        return self.temas

    def get_select_categorias(self):
        self.selectTemas = []
        for tema, valor in self.temas.items():
            if valor == True:
                self.selectTemas.append(tema.upper())
        return self.selectTemas

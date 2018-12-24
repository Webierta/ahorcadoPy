import configparser

#-------------------------------------------------------------------------
# clase: Datos(object)
#-------------------------------------------------------------------------
class Datos(object):

    def __init__(self):
        self.cfg = configparser.ConfigParser()
        self.cfg["Marcador"] = {"victorias": "0", "derrotas": "0"}
        self.cfg["Opciones"] = {"nivel": "Avanzado", "sonido": "True"}
        try:
            self.cfg.read("config.cfg")
        except:
            self.guardar_cfg()

    def guardar_cfg(self):
        with open("config.cfg", "w") as archivoconfig:
            self.cfg.write(archivoconfig)

    @property
    def victorias(self):
        return int(self.cfg["Marcador"].get("victorias"))

    @property
    def derrotas(self):
        return int(self.cfg["Marcador"].get("derrotas"))

    @property
    def nivel(self):
        return self.cfg["Opciones"].get("nivel")

    @property
    def sonido(self):
        return self.cfg.getboolean("Opciones", "sonido")

    def guardar_marcador(self, v=0, d=0):
        self.cfg.set("Marcador", "victorias", str(self.victorias + v))
        self.cfg.set("Marcador", "derrotas", str(self.derrotas + d))
        self.guardar_cfg()

    def reset_marcador(self):
        self.cfg.set("Marcador", "victorias", str(0))
        self.cfg.set("Marcador", "derrotas", str(0))
        self.guardar_cfg()

    def guardar_sonido(self, sond):
        self.cfg.set("Opciones", "sonido", str(sond))
        self.guardar_cfg()

    def guardar_nivel(self, nivel):
        self.cfg.set("Opciones", "nivel", nivel)
        self.guardar_cfg()

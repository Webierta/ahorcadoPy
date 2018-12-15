import configparser

#-------------------------------------------------------------------------
# clase: Datos()
#-------------------------------------------------------------------------
class Datos:

    def guardar_cfg(self):
        with open("config.cfg", "w") as archivoconfig:
            self.cfg.write(archivoconfig)

    def __init__(self):
        self.cfg = configparser.ConfigParser()
        self.cfg["Marcador"] = {
            "victorias": "0", "derrotas": "0"}
        self.cfg["Opciones"] = {"nivel": "Avanzado", "sonido": "True"}

        try:
            self.cfg.read("config.cfg")
        except:
            self.guardar_cfg()

        self.victorias = int(self.cfg["Marcador"].get("victorias"))
        self.derrotas = int(self.cfg["Marcador"].get("derrotas"))
        self.nivel = self.cfg["Opciones"].get("nivel")
        self.sonido = self.cfg.getboolean("Opciones", "sonido")

    def guardar_marcador(self, v=0, d=0):
        if v == 1:
            self.victorias += 1
        if d == 1:
            self.derrotas += 1
        self.cfg.set("Marcador", "victorias", str(self.victorias))
        self.cfg.set("Marcador", "derrotas", str(self.derrotas))
        self.guardar_cfg()

    def reset_marcador(self):
        self.victorias = 0
        self.derrotas = 0
        self.cfg.set("Marcador", "victorias", str(self.victorias))
        self.cfg.set("Marcador", "derrotas", str(self.derrotas))
        self.guardar_cfg()

    def guardar_sonido(self, sond):
        self.sonido = sond
        self.cfg.set("Opciones", "sonido", str(self.sonido))
        self.guardar_cfg()

    def guardar_nivel(self, nivel):
        self.nivel = nivel
        self.cfg.set("Opciones", "nivel", self.nivel)
        self.guardar_cfg()

    def get_nivel(self):
        return self.nivel

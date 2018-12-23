from ahorcado.datos import Datos
from ahorcado.palabra import Palabra

#-------------------------------------------------------------------------
# clase: Juego(object)
#-------------------------------------------------------------------------
class Juego(object):

    def __init__(self):
        self.datos = Datos()
        self.buscar_palabra = Palabra()
        if self.datos.nivel != "Temas":
            self.buscar_palabra.online_nivel()
        else:
            self.buscar_palabra.vocabulario()
        self.palabra = self.buscar_palabra.palabra
        self.pista = self.buscar_palabra.pista
        self.lista = list(len(self.palabra) * "_")
        self.fallos = 0

    @property
    def secreta(self):
        return len(self.palabra) * "_"

    def checkLetra(self, letra):
        for index, item in enumerate(self.palabra):
            if item == letra:
                self.lista[index] = letra
        return self.lista

    def sumaError(self):
        self.fallos += 1
        return self.fallos

    def checkVictoria(self, listaCheck):
        if self.palabra == ("".join(listaCheck)):
            return True
        return False

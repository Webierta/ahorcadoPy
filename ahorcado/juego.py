from ahorcado.datos import Datos
from ahorcado.palabra import Palabra

#-------------------------------------------------------------------------
# clase: Juego()
#-------------------------------------------------------------------------
class Juego:

    def __init__(self):
        self.pista = ""
        self.palabra = ""
        self.datos = Datos()
        self.nivel = self.datos.get_nivel()
        self.buscar_palabra = Palabra()
        self.fallos = 0

        if self.nivel != "Temas":
            self.buscar_palabra.online_nivel()
            self.palabra = self.buscar_palabra.get_palabra()
        else:
            self.buscar_palabra.vocabulario()
            self.palabra = self.buscar_palabra.get_palabra()
            self.pista = self.buscar_palabra.get_pista()

        # Ocultar palabra
        if self.palabra != "":
            self.secreta = len(self.palabra) * "_"
            self.lista = list(self.secreta)

    def checkLetra(self, letra):
        if letra not in self.palabra:
            return False
        index = 0
        while index < len(self.palabra):
            if self.palabra[index] == letra:
                self.lista[index] = letra
            index += 1
        return self.lista

    def sumaError(self):
        self.fallos += 1
        return self.fallos

    def checkVictoria(self, listaCheck):
        if self.palabra == ("".join(listaCheck)):
            return True
        return False

    def get_palabra(self):
        return self.palabra

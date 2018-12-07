from random import choice

from ahorcado.datos import Datos
from ahorcado.palabras import Vocabulario

#-------------------------------------------------------------------------
# clase: Juego()
#-------------------------------------------------------------------------
class Juego:

    def __init__(self):
        self.temasJuego = []
        self.pista = ""
        self.palabra = ""
        self.datos = Datos()
        self.fallos = 0

        self.vocabulario = Vocabulario()
        self.todosTemas =self.vocabulario.todosTemas

        # Obtener nombres de los temas seleccionados
        self.nombresCategorias = self.datos.get_select_categorias()

        # Temas seleccionados
        self.temasJuego = []
        for tema in self.todosTemas:
            for ele in self.nombresCategorias:
                if tema["CATEGORIA"] == ele:
                    self.temasJuego.append(tema)

        # Tema aleatorio: obtener su pista y una palabra aleatoria
        self.categoria = choice(self.temasJuego)
        self.pista = self.categoria["PISTA"]
        self.palabra = choice(self.categoria["PALABRAS"])

        # Ocultar palabra
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

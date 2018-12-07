import os
import sys
import json

#-------------------------------------------------------------------------
# clase: Juego()
#-------------------------------------------------------------------------
class Vocabulario:

    def __init__(self):
        # ALMACEN DE PALABRAS
        filePalabras = os.path.join(os.path.dirname(__file__),
            "resources/txt/vocabulario.json")
        try:
            with open(filePalabras, "r") as archivoPalabras:
                dataPalabras = json.load(archivoPalabras)
        except:
            print("ERROR: ARCHIVO DE PALABRAS CORRUPTO O NO ENCONTRADO.")
            sys.exit(1)

        self.todosTemas = dataPalabras["VOCABULARIO"]

    # Función que retorna todas las categorias
    def all_categorias(self):
        self.temasTotal = []
        for elemento in self.todosTemas:
            self.temasTotal.append(elemento["CATEGORIA"])
        return self.temasTotal


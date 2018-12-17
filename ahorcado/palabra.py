import os
import json
from random import choice

from urllib.request import Request, urlopen  # import urllib.request
from urllib.error import URLError, HTTPError
import re
from unicodedata import normalize

from ahorcado.datos import Datos

#-------------------------------------------------------------------------
# clase: Palabra()
#-------------------------------------------------------------------------
class Palabra:

    def __init__(self):
        self.palabra = ""
        self.pista = ""
        self.datos = Datos()
        self.error_match = 0

    def online_nivel(self):  # def online_nivel(self, niv):
        url1 = "https://www.palabrasaleatorias.com/?fs=1&fs2="
        url2 = "&Submit=Nueva+palabra"
        nivel = self.datos.get_nivel()
        if nivel == "Avanzado":
            self.url = url1 + "0" + url2
        else:
            self.url = url1 + "1" + url2
        headers = {'User-Agent':
            "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:48.0) Gecko/20100101 Firefox/48.0"}
        try:
            req = Request(self.url, headers = headers)
            source = urlopen(req).read()  #.decode('utf-8')
        except HTTPError as e:
            print('HTTP Error: ', e.code)
            self.cambiar_vocabulario()
        except URLError as e:
            print('URL Error: ', e.reason)
            self.cambiar_vocabulario()
        except:
            print("Error de conexión")
            self.cambiar_vocabulario()
        else:
            self.online(source)

    def online(self, source):
        regex = '<br><div style=\"font-size:3em; color:#6200C5;\">.\n([a-zA-Z]*?)<\/div>.\n'
        #regex = '<br><div style=\"font-size:3em; color:#6200C5;\">.\n(.*?)<\/div>.\n'
        html = source.decode("utf-8")
        matches = re.findall(regex, html)
        if matches:
            text_div = matches[0]
            text_div = text_div.encode('utf-8').decode('unicode_escape')
            palabra_online = text_div.encode("latin-1").decode("utf-8")
            palabra_online = re.sub(
                r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+",
                r"\1", normalize( "NFD", palabra_online), 0, re.I)
            palabra_online = normalize("NFC", palabra_online)
            palabra_online = palabra_online.upper()
            if (((len(palabra_online) > 2) and (len(palabra_online) < 13)) and
                palabra_online.isalpha()):
                self.palabra = palabra_online
                self.error_match = 0
            else:
                self.cont_error_match()
        else:  # SIN CAPTURAS DE DATOS
            self.cont_error_match()

    def cont_error_match(self):
        self.error_match += 1
        if self.error_match > 2:
            self.cambiar_vocabulario()
        else:
            self.online_nivel()

    def cambiar_vocabulario(self):
        self.datos.guardar_nivel("Temas")

    def vocabulario(self):
        filePalabras = os.path.join(os.path.dirname(__file__),
            "resources/txt/vocabulario.json")
        try:
            with open(filePalabras, "r") as archivoPalabras:
                dataPalabras = json.load(archivoPalabras)
        except:
            print("ERROR: ARCHIVO DE PALABRAS CORRUPTO O NO ENCONTRADO.")
            self.palabra = "AHORCADO"  # sys.exit(1)
            self.pista = ("La aplicación está utilizando una palabra comodín "
                "porque posiblemente el archivo de palabras está corrupto o no "
                "ha sido encontrado.\n\nPrueba a jugar en otro nivel o descarga "
                "nuevamente la aplicación desde la web del proyecto.")
        else:
            self.todosTemas = dataPalabras["VOCABULARIO"]
            self.categoria = choice(self.todosTemas)
            self.pista = self.categoria["PISTA"]
            self.palabra = choice(self.categoria["PALABRAS"])

    def get_palabra(self):
        return self.palabra

    def get_pista(self):
        return self.pista

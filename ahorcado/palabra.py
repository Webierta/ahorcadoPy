import json
from random import choice
from urllib.request import Request, urlopen  # import urllib.request
from urllib.error import URLError, HTTPError
import re
from unicodedata import normalize

from ahorcado.datos import Datos
from ahorcado.archivos import files

#-------------------------------------------------------------------------
# clase: Palabra(object)
#-------------------------------------------------------------------------
class Palabra(object):

    def __init__(self):
        self.palabra = ""
        self.pista = ""
        self.datos = Datos()
        self.error_match = 0

    def online_nivel(self):
        url1 = "https://www.palabrasaleatorias.com/?fs=1&fs2="
        url2 = "&Submit=Nueva+palabra"
        niveles = {"Avanzado": "0", "Júnior": "1"}
        headers = {'User-Agent':
            "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:48.0) Gecko/20100101 Firefox/48.0"}
        try:
            url = url1 + niveles[self.datos.nivel] + url2
            req = Request(url, headers = headers)
            source = urlopen(req).read()  #.decode('utf-8')
        except (HTTPError, URLError) as e:
            print("Error:", e)
            self.datos.guardar_nivel("Temas")
        except:
            print("Error de conexión")
            self.datos.guardar_nivel("Temas")
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
            self.datos.guardar_nivel("Temas")
        else:
            self.online_nivel()

    def vocabulario(self):
        filePalabras = files.get("vocabulario", "ERROR")
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

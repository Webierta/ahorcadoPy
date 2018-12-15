import os
import json
from random import choice

import requests
from lxml import html
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

    def online_nivel(self, niv):
        url1 = "https://www.palabrasaleatorias.com/?fs=1&fs2="
        url2 = "&Submit=Nueva+palabra"
        url = url1 + niv + url2
        headers = {"user-agent":
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36"}
        try:
            self.page = requests.get(url, headers=headers, timeout=5)
        except requests.ConnectionError as e:
            print("OOPS!! Error de conexión. Asegúrate de estar conectado a internet.\n")
            print(str(e))
            self.cambiar_vocabulario()
        except requests.Timeout as e:
            print("OOPS!! Error por tiempo de conexión superado.")
            print(str(e))
            self.cambiar_vocabulario()
        except requests.RequestException as e:
            print("OOPS!! Error.")
            print(str(e))
            self.cambiar_vocabulario()
        except KeyboardInterrupt:
            print("Programa interrumpido.")
            self.cambiar_vocabulario()
        else:
            self.online()

    def online(self):
        status_code = self.page.status_code
        if status_code != 200:
            self.cambiar_vocabulario()
        if status_code == 200:
            html_page = html.fromstring(self.page.content)  # html_page = page.text
            html_div = html_page.xpath('//div[@style="font-size:3em; color:#6200C5;"]/text()')
            if html_div:
                text_div = html_div[0]
                text_div = text_div.encode('utf-8').decode('unicode_escape')
                text_div = text_div[2:]
                palabra_online = text_div.encode("latin-1").decode("utf-8")
                palabra_online = re.sub(
                    r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+",
                    r"\1", normalize( "NFD", palabra_online), 0, re.I)
                palabra_online = normalize("NFC", palabra_online)
                palabra_online = palabra_online.upper()
                self.palabra = palabra_online
            else:  # SIN CAPTURAS DE DATOS
                self.cambiar_vocabulario()

    def cambiar_vocabulario(self):
        self.datos = Datos()
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

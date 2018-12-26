import sys
import os

# key: ruta parcial a archivo
dicFiles = {
    "help": "resources/txt/HELP.rst",
    "about": "resources/txt/ABOUT.rst",
    "titulo": "resources/img/ahorcado.png",
    "icono": "resources/img/icon128.png",
    "paypal": "resources/img/donate.gif",
    "pista": "resources/img/pista.png",
    "marcador": "resources/img/marcador.png",
    "triunfos": "resources/img/triunfos.png",
    "derrotas": "resources/img/derrotas.png",
    "error": "resources/media/error.wav",
    "acierto": "resources/media/acierto.wav",
    "gameover": "resources/media/gameover.wav",
    "victoria": "resources/media/victoria.wav",
    "vocabulario": "resources/txt/vocabulario.json",
    "tecla": "resources/media/tecla.wav"
}

# key: ruta completa a archivo
files = {key: os.path.join(os.path.dirname(__file__), val)
    for key, val in dicFiles.items()}

# Rutas completas a los archivos de imagen de la horca
filesHorca = [os.path.join(os.path.dirname(__file__),
    "resources/img/" + str(x) + ".png") for x in range(1, 8)]

# Comprueba las rutas de todos los archivos
def comprueba_archivo(archivos):
    for archivo in archivos:
        if not os.path.isfile(archivo):
            print("ERROR: ARCHIVO {} NO ENCONTRADO.".format(archivo))
            sys.exit(1)

filesRutas = [archivo for archivo in files.values()]
comprueba_archivo(filesRutas)
comprueba_archivo(filesHorca)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# name:         ahorcado.py / __init__.py (Python 3.x).
# description:  Aplicación de escritorio que revive el clásico juego de lápiz y
#               papel 'El Ahorcado'.
# author:       Jesús Cuerda Villanueva, https://github.com/Webierta
# version:      0.1.1 Diciembre 2018
#
#-------------------------------------------------------------------------

import sys
try:
    import tkinter as tk
except ImportError:
    print("Se requiere el modulo tkinter. Más información en about.txt")
    sys.exit(1)

from main import StartPage
from main import *
from juego import *
from datos import *
__all__ = ["Base", "StartPage", "Game", "Marcador", "Juego", "Datos"]

def main():
    root = tk.Tk()
    StartPage(root)
    
#import subprocess
#subprocess.run(["python", "__init__.py"], input=main(), stdout=subprocess.PIPE)

if __name__ == "__main__":
    main()
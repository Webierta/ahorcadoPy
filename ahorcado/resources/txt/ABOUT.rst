Juego del Ahorcado (versión 0.1.2 - 2018)
=========================================

Aplicación de escritorio que revive el clásico juego de lápiz y papel 'El Ahorcado'

Copyleft 2018 - Jesús Cuerda - Todos los errores reservados.

Web: https://github.com/Webierta/ahorcadoPy

Aplicación gratuita y sin publicidad. Colabora con un donativo vía PayPal.

Software libre de código abierto sujeto a la GNU General Public License v.3, distribuido con la esperanza de que sea entretenido, pero SIN NINGUNA GARANTÍA. Todos los errores reservados.


REQUISITOS DEL SISTEMA
----------------------

- Python versión 3.x. Requiere que el sistema tenga instalado Python versión 3.x, disponible en python.org para distintas plataformas: Windows, Linux/UNIX, Mac OS X y otras. Python se encuentra instalado por defecto en la mayoría de sistemas GNU/Linux si bien en muchas ocasiones se trata de una versión 2.x. La versión 3.x suele estar incluida en los repositorios de casi todas las distribuciones linux, por lo que su instalación es sencilla. La aplicación sólo utiliza componentes de la librería estándar de Python.

- El paquete 'tkinter' para Python. Actualmente se incluye con todas las distribuciones estándar de Python3.x. Este paquete ofrece la interfaz estándar de Python para el conjunto de herramientas gráficas. En Windows ya se instaló cuando instalaste Python 3. Aunque tkinter es parte de la biblioteca estándar de Python, muchas distribuciones linux lo empaquetan por separado del paquete principal de Python. Para comprobar si está instalado en tu sistema, desde consola: $ python3, y luego >>>import tkinter

  Si aparece un mensaje de error, tkinter no está instalado. En los repositorios de la mayoría de distribuciones linux lo encontrarás con el nombre python3-tk (o simplemente tk).

  Puedes comprobar si has instalado 'tkinter' correctamente ejecutando estos comandos (Alguno de ellos debería abrir una ventana de demostración de la interfaz gráfica de tkinter):

    python3 -m tkinter

    tkinter._test()


INSTALACIÓN / EJECUCIÓN
-----------------------
Puedes instalarlo o simplemente ejecutar sin instalar:


INSTALAR
::::::::

Si te sientes cómodo con pip, descarga el archivo comprimido y ejecuta preferiblemente en un entorno virtual:

  $ pip install ahorcado-0.1.1.tar.gz
o
  $ pip3 install ahorcado-0.1.1.tar.gz

Y después arranca la aplicación con:

  $ ahorcado


EJECUCIÓN
:::::::::

Para ejecutar el juego sin instalarlo, descarga el repositorio comprimido (zip), descomprime y desde consola (en Windows la abres con cmd) desplázate y entra en el directorio principal (ahorcadoPy) y escribe:

  $ python -m ahorcado.main
o
  $ python3 -m ahorcado.main


DESARROLLO
----------

Aplicación con lenguaje de programación python 3 e interfaz gráfica tkinter.

0.1.2
  Diciembre 2018: Empaquetado para distribución e instalación con pip

0.1.1
  Diciembre 2018: Archivo de configuración y efectos sonoros (linux)

0.1.0
  Noviembre 2018: Publicada primera versión


RECONOCIMIENTOS
---------------

- Banco de imágenes y sonidos del Instituto de Tecnologías Educativas. Ministerio de Educación.
- Noun Project.
- Flaticon: Picol, Freepik, Tuts+, Icomoon, Daniel Bruce, Amit Jakhu.


LICENCIA
--------

Copyleft 2018, Jesús Cuerda Villanueva. All Wrongs Reserved

Software libre de código abierto sujeto a la GNU General Public License v.3. EL AHORCADO es software libre distribuido con la esperanza de que sea útil, pero SIN NINGUNA GARANTÍA.

This file is part of EL AHORCADO.

EL AHORCADO is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation either version 3 of the License.

EL AHORCADO is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details. https://www.gnu.org/licenses/gpl-3.0.txt
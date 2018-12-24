Juego del Ahorcado (versión 0.2.3 - 2018)
=========================================

Aplicación de escritorio que revive el clásico juego de lápiz y papel 'El Ahorcado'

Copyleft 2018 - Jesús Cuerda - Todos los errores reservados.

Web: https://github.com/Webierta/ahorcadoPy

Aplicación gratuita y sin publicidad. Colabora con un donativo vía PayPal.

Software libre de código abierto sujeto a la GNU General Public License v.3, distribuido con la esperanza de que sea entretenido, pero SIN NINGUNA GARANTÍA. Todos los errores reservados.


REQUISITOS DEL SISTEMA
----------------------

- Python versión 3.x. Requiere que el sistema tenga instalado Python versión 3.x, disponible en python.org para distintas plataformas: Windows, Linux/UNIX, Mac OS X y otras. Python se encuentra instalado por defecto en la mayoría de sistemas GNU/Linux si bien en muchas ocasiones se trata de una versión 2.x. La versión 3.x suele estar incluida en los repositorios de casi todas las distribuciones linux, por lo que su instalación es sencilla. La aplicación solo utiliza componentes de la librería estándar de Python, sin ninguna dependencia de librerías de terceros.

- El paquete 'tkinter' para Python. Actualmente se incluye con todas las distribuciones estándar de Python3.x. Este paquete ofrece la interfaz estándar de Python para el conjunto de herramientas gráficas. En Windows ya se instaló cuando instalaste Python 3. Aunque tkinter es parte de la biblioteca estándar de Python, muchas distribuciones linux lo empaquetan por separado y en los repositorios de la mayoría de distribuciones linux lo encontrarás con nombres como python3-tk o simplemente tk.

- Conexión a internet solo en los niveles «Avanzado» y «Júnior». También es posible jugar sin conexión a internet en el nivel «Temas».

INSTALACIÓN / EJECUCIÓN
-----------------------
Puedes instalarlo o simplemente ejecutar sin instalar:

INSTALAR
::::::::

Descarga el archivo comprimido e instala con pip (preferiblemente en un entorno virtual). Por ejemplo, ejecuta (actualiza con los datos de la última versión):

  $ pip install ahorcado-0.1.1.tar.gz
o
  $ pip3 install ahorcado-0.1.1.tar.gz

Y después arranca la aplicación con:

  $ ahorcado


EJECUCIÓN
:::::::::

Asegúrate de cumplir los requisitos. Para ejecutar el juego sin instalarlo, descarga el repositorio comprimido (zip), descomprime y desde consola (en Windows la abres con cmd) desplázate y entra en el directorio principal (ahorcadoPy) y escribe:

  $ python -m ahorcado.main
o
  $ python3 -m ahorcado.main


DESARROLLO
----------

Aplicación con lenguaje de programación python 3 e interfaz gráfica tkinter.

0.2.3
  Diciembre 2018: Interfaz gráfica mejorada

0.2.2
  Diciembre 2018: Código optimizado y "pythonizado" (estilo más "pythonico").

0.2.1
  Diciembre 2018: Eliminación de dependencias de librerías de terceros.

0.2.0
  Diciembre 2018: Generación de palabras online y nuevos niveles de dificultad.

0.1.3
  Diciembre 2018: Añadida opción de temas.

0.1.2
  Diciembre 2018: Empaquetado para distribución e instalación con pip

0.1.1
  Diciembre 2018: Archivo de configuración y efectos sonoros (linux)

0.1.0
  Noviembre 2018: Publicada primera versión


RECONOCIMIENTOS
---------------

- Generador de palabras aleatorias online: palabrasaleatorias.com
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

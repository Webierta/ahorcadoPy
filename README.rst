
El ahorcado
===========

.. image:: https://raw.githubusercontent.com/Webierta/ahorcadoPy/master/resources/img/icon128.png
   :alt: El ahorcado


Juego del Ahorcado (versión 0.1.1 - 2018)

Aplicación de escritorio que revive el clásico juego de lápiz y papel 'El Ahorcado'

Copyleft 2018 - Jesús Cuerda - Todos los errores reservados.

Web: `https://github.com/Webierta/ahorcadoPy <https://github.com/Webierta/ahorcadoPy>`_

Aplicación gratuita y sin publicidad. Colabora con un donativo vía PayPal.

Software libre de código abierto sujeto a la GNU General Public License v.3, distribuido con la esperanza de que sea entretenido, pero SIN NINGUNA GARANTÍA. Todos los errores reservados.

----


REQUISITOS DEL SISTEMA
----------------------

- **Python versión 3.x**. Requiere que el sistema tenga instalado Python versión 3.x, disponible en python.org para distintas plataformas: Windows, Linux/UNIX, Mac OS X y otras. Python se encuentra instalado por defecto en la mayoría de sistemas GNU/Linux si bien en muchas ocasiones se trata de una versión 2.x. La versión 3.x suele estar incluida en los repositorios de casi todas las distribuciones linux, por lo que su instalación es sencilla. La aplicación sólo utiliza componentes de la librería estándar de Python.

- **El paquete 'tkinter' para Python**. Actualmente se incluye con todas las distribuciones estándar de Python3.x. Este paquete ofrece la interfaz estándar de Python para el conjunto de herramientas gráficas. En Windows ya se instaló cuando instalaste Python 3. Aunque tkinter es parte de la biblioteca estándar de Python, muchas distribuciones linux lo empaquetan por separado del paquete principal de Python. Para comprobar si está instalado en tu sistema, desde consola: $ python3, y luego >>>import tkinter

  Si aparece un mensaje de error, tkinter no está instalado. En los repositorios de la mayoría de distribuciones linux lo encontrarás con el nombre python3-tk (o simplemente tk).

  Puedes comprobar si has instalado 'tkinter' correctamente ejecutando estos comandos:

  .. code-block:: bash

    python3 -m tkinter
    tkinter._test()

  Alguno de ellos debería abrir una ventana de demostración de la interfaz gráfica de tkinter.


EJECUCIÓN
---------

1) Comprueba que tu sistema cumple los requisitos necesarios para la correcta ejecución de la aplicación.
2) Descarga el archivo comprimido con la última versión, descomprime y copia la carpeta principal llamada 'ahorcado' a cualquier lugar de tu sistema.
3) En muchos sistemas, puedes ejecutarlo desde el entorno gráfico haciendo doble clic en el archivo **__init__.py**. Si no funciona, comprueba las preferencias de tu administrador de archivos: por ejemplo, en Nautilus, en Preferencias --> Comportamiento, selecciona 'Ejecutar los archivos de texto ejecutables al abrirlos'. También puedes probar haciendo clic con el botón secundario del ratón y seleccionar "Ejecutar" o "Abrir" o bien "Abrir con..." y luego «Python(v3.x)».
4) Para ejecutarlo desde consola (en Windows la abres con cmd), desplázate al directorio donde se encuentra la carpeta principal y ejecuta:

  - en *linux*: **python3 __init__.py**. También funciona con: **./__init__.py**
  - en *Windows*, dependiendo de la versión y de la configuración: **__init__.py** o bien **python __init__.py**


DESARROLLO
----------

Aplicación con lenguaje de programación python 3 e interfaz gráfica tkinter.

0.1.1
  Diciembre 2018  Archivo de configuración y efectos sonoros (linux)

0.1.0
  Noviembre 2018  Publicada primera versión


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

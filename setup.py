from setuptools import setup, find_packages

with open("README.rst", encoding="utf-8") as df:
    ld = df.read()

setup(
    name="ahorcado",
    version="0.1.2",
    description="Aplicación que revive el clásico juego de lápiz y papel 'El Ahorcado'",
    long_description=ld,
    author="Jesús Cuerda",
    url="https://github.com/Webierta",
    license="GNU GPLv3",
    packages=find_packages(),
    # package_data={
    #     "resources": [
    #         "img/*.png",
    #         "media/*.wav"]
    # },
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Topic :: Games/Entertainment",
        "Natural Language :: Spanish"
    ],
    entry_points = {
        "console_scripts":[
            "ahorcado = ahorcado.main:main",
        ]
    }
)

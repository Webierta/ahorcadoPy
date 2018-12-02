from random import choice

#-------------------------------------------------------------------------
#
# clase: Juego()
#
#-------------------------------------------------------------------------
class Juego:

    def __init__(self):

        # ALMACEN DE PALABRAS
        ANIMALES = ["ABEJA", "ABEJORRO", "AGUILA", "ALMEJA",
            "ANACONDA", "ARAÑA", "ASNO", "ATUN", "AVESTRUZ", "AVISPA", "BALLENA",
            "BESUGO", "BUFALO", "BUHO", "BUITRE", "BURRO", "CABALLO", "CABRA",
            "CAIMAN", "CAMALEON", "CAMELLO", "CANARIO", "CANGREJO", "CARACOL",
            "CEBRA", "CERDO", "CIERVO", "CIGALA", "COBRA", "CONEJO", "COTORRA",
            "COYOTE", "DELFIN", "ELEFANTE", "FOCA", "GACELA", "GALLO", "GACELA",
            "GARZA", "GATO", "GAVILAN", "GAVIOTA", "GORILA", "GORRION", "GRILLO",
            "GUEPARDO", "GUSANO", "HALCON", "HAMSTER", "HIENA", "HORMIGA",
            "IGUANA", "JABALI", "JAGUAR", "JINETA", "JIRAFA", "KOALA",
            "LAGARTO", "LANGOSTA", "LECHUZA", "LEON", "LEOPARDO", "LEMUR",
            "LIBELULA", "LIEBRE", "LINCE", "LLAMA", "LOBO", "LOMBRIZ", "LORO",
            "MARIPOSA", "MARMOTA", "MARSOPA", "MEJILLON", "MONO", "MOSCA",
            "MULA", "NUTRIA", "ORCA", "OSO", "OSTRA", "OVEJA", "PALOMA",
            "PANTERA", "PATO", "PAVO", "PERDIZ", "PERRO", "PINGUINO", "PITON",
            "PULGA", "PULPO", "PUMA", "RANA", "RATON", "SALMON", "SAPO",
            "TIBURON", "TIGRE", "TOPO", "TORO", "TORTUGA", "TRUCHA", "TUCAN",
            "VACA", "VIBORA", "ZORRO"]
        COLORES = ["AZUL", "AMARILLO", "VIOLETA", "MARRON",
            "ROJO", "BLANCO", "NEGRO", "GRIS", "MORADO", "NARANJA", "VERDE",
            "AMBAR", "AÑIL", "BEIGE", "BEIS", "CARMESI", "CELESTE", "COLORADO",
            "CREMA", "ESCARLATA", "FUCSIA", "ROSA", "GRANATE", "LILA", "MAGENTA",
            "OCRE", "PURPURA"]
        FLORES = ["AMAPOLA", "ROSA", "CLAVEL", "MARGARITA",
            "AZALEA", "CAMELIA", "GERANIO", "JAZMIN", "LIRIO", "ORQUIDEA",
            "NARCISO", "TULIPAN", "NENUFAR", "GIRASOL", "DALIA"]
        DEPORTES = ["AEROBIC", "AJEDREZ", "ARCO", "BILLAR",
            "BOLOS", "BOXEO", "BEISBOL", "CICLISMO", "CRICKET", "ESCALADA",
            "ESGRIMA", "ESQUI", "FUTBOL", "GOLF", "GIMNASIA", "HIPICA", "HOCKEY",
            "JUDO", "KARATE", "LUCHA", "NATACION", "PADDLE", "PATINAJE", "PETANCA",
            "PINGPONG", "POLO", "RUGBY", "TENIS", "TIRO", "VOLEIBOL"]
        ALIMENTOS = ["QUESO", "PIZZA", "CHORIZO", "JAMON",
            "SALAMI", "PAELLA", "PASTEL", "BIZCOCHO", "MACARRONES", "MENESTRA",
            "ENSALADA", "SOPA", "CHOCOLATE", "SALSA", "HUEVO", "CREMA", "LECHE",
            "GUARNICIÓN", "CHULETA", "FLAN", "CEVICHE", "COCIDO", "TORTILLA",
            "TARTA", "PURE", "ALBONDIGA", "GAZPACHO", "TORTITA", "TACO",
            "BOCADILLO", "TORREZNO", "FIDEUA", "CROQUETA", "SALMOREJO", "EMPANADA",
            "SANDWICH", "PISTO", "FABADA", "ESCALIBADA", "LENTEJAS", "CHURRO",
            "ENSAIMADA", "MORCILLA", "YOGUR", "TURRON", "PAPAS", "PORRUSALDA",
            "CALLOS", "TORRIJA", "BUTIFARRA"]
        QUIMICOS = ["LITIO", "HELIO", "FOSFORO", "AZUFRE",
            "NIQUEL", "HIERRO", "PLATA", "MERCURIO", "POLONIO", "PLOMO", "FLUOR",
            "HIDROGENO", "CARBONO", "OXIGENO", "SODIO", "MAGNESIO", "ALUMINIO",
            "SILICIO", "CLORO", "POTASIO", "CALCIO", "TITANIO", "COBALTO",
            "COBRE", "ZINC", "ESTRONCIO", "CADMIO", "YODO", "ESTAÑO", "PLATINO",
            "RADON", "URANIO", "MOLIBDENO"]
        VEHICULOS = ["COCHE", "MOTO", "BICICLETA", "TREN",
            "BARCO", "AVION", "HELICOPTERO", "AUTOBUS", "AUTOMOVIL", "TRINEO",
            "CARRUAJE", "YATE", "LANCHA", "SUBMARINO", "CANOA", "AVIONETA",
            "PARAPENTE", "COHETE", "METRO", "TRANVIA", "FUNICULAR", "FERROCARRIL",
            "CAMION", "CAMIONETA", "TRACTOR", "MOTOCARRO", "FURGONETA", "BUQUE",
            "KAYAK", "PIRAGUA", "VELERO", "CARRO", "CARROZA", "MONOPATIN",
            "TRICICLO"]
        CUERPO = ["BRAZO", "MANO", "CABEZA", "PIERNA",
            "CUELLO", "CADERA", "RODILLA", "DEDO", "OREJA", "NARIZ", "CARA", "CODO",
            "OMBLIGO", "ESPALDA", "TOBILLO", "GARGANTA", "CEJA", "MEJILLA",
            "BOCA", "BARBILLA", "LENGUA", "PARPADO", "PESTAÑA", "HOMBRO",
            "MUÑECA", "PULGAR", "MUSLO", "TALON", "CEREBRO", "CORAZON", "HIGADO",
            "RIÑON", "PULMON", "PANCREAS", "VEJIGA", "CINTURA", "PECHO", "PIEL",
            "DIENTE", "NALGA"]
        PRENDAS = ["ABRIGO", "GUANTE", "BUFANDA", "CAMISA",
            "CALCETIN", "CORBATA", "PANTALON", "FALDA", "CAMISETA", "ZAPATO",
            "SOMBRERO", "MEDIA", "CHAQUETA", "CINTURON", "BLUSA", "GORRO",
            "SUETER", "JERSEY", "TRAJE", "BOINA", "VESTIDO", "BOTA", "SANDALIA",
            "CHANCLA", "CORREA", "LIGA"]
        OFICIOS = ["MEDICO", "ENFERMERO", "MAESTRO",
            "PINTOR", "ALBAÑIL", "ABOGADO", "ZAPATERO", "PSICOLOGO", "FONTANERO",
            "CARPINTERO", "BANQUERO", "PROFESOR", "MECANICO", "PERIODISTA",
            "JUEZ", "ELECTRICISTA", "ESCRITOR", "INFORMATICO", "PORTERO", "POLICIA",
            "DENTISTA", "FUTBOLISTA", "CHOFER", "SASTRE", "CERRAJERO", "PASTOR",
            "AGRICULTOR", "CARNICERO", "PANADERO", "DEPENDIENTE", "INGENIERO",
            "ARQUITECTO", "MATEMATICO", "BIOLOGO", "FISICO", "QUIMICO", "FILOSOFO",
            "ARQUEOLOGO", "FARMACEUTICO", "GEOGRAFO", "HISTORIADOR", "SOCIOLOGO",
            "MUSICO", "ECONOMISTA", "RADIOLOGO", "GANADERO"]
        NUMEROS = ["QUINCE", "DOCE", "TRECE", "CATORCE",
            "SIETE", "CIEN", "SIETE", "OCHO", "NUEVE", "DIEZ", "CERO", "CUATRO",
            "CINCO", "TREINTA", "CUARENTA", "CINCUENTA", "MILLON", "SESENTA",
            "SETENTA", "OCHENTA", "NOVENTA"]
        CIUDADES = ["ADELAIDA", "AGRA", "ALBACETE", "ALEPO", "ALICANTE", "ANKARA",
            "ATENAS", "ATLANTA", "AVILA", "BADAJOZ", "BAGDAD", "BANGKOK", "BASORA",
            "BERLIN", "BERNA", "BILBAO", "BOGOTA", "BOMBAY", "BOSTON", "BRUSELAS",
            "BURGOS", "CACERES", "CADIZ", "CALCUTA", "CARACAS", "CHICAGO", "COLONIA",
            "CORDOBA", "CUENCA", "DALLAS", "DAKAR", "DAMASCO", "DETROIT", "DUBAI",
            "DUBLIN", "ESTAMBUL", "GINEBRA", "HAMBURGO", "HANOI", "HOUSTON", "IBIZA",
            "JAEN", "KABUL", "KARACHI", "LEIPZIG", "LEON", "LIMA", "LISBOA", "LONDRES",
            "MADRID", "MALAGA", "MANILA", "MEDELLIN", "MERIDA", "MILAN", "MOSCU",
            "MUNICH", "MURCIA", "NAGOYA", "NAIROBI", "NAPOLES", "OPORTO", "OSAKA",
            "OSLO", "PALENCIA", "PARIS", "PEKIN", "PRAGA", "RABAT", "RIAD", "ROMA",
            "SANTIAGO", "SEGOVIA", "SEUL", "SEVILLA", "SHANGHAI", "SIDNEY", "SINGAPUR",
            "SOFIA", "TEHERAN", "TOKIO", "TOLEDO", "TORONTO", "TUNEZ", "VALENCIA",
            "VENECIA", "VIENA", "YAKARTA", "ZAMORA", "ZARAGOZA"]
        PELICULAS = ["AGORA", "AKIRA", "ALIEN", "ALIENTO", "AMADEUS", "AMELIE",
            "ARDOR", "ARREBATO", "ASESINOS", "AVATAR", "BABEL", "BABYLON", "BAMBI",
            "BATMAN", "BICHOS", "BLACULA", "BLADE", "BOLERO", "BOLT", "BRAVE", "BRICK",
            "BROTHERS", "BRUNO", "BURIED", "CABARET", "CALABUCH", "CAMINO", "CANDIDA",
            "CANDYMAN", "CAPOTE", "CARRIE", "CARS", "CASINO", "CATWOMAN", "CHAPLIN",
            "CHICAGO", "CLUEDO", "CONTROL", "CYBORG", "DAISY", "DRACULA", "EDTV",
            "ELEGY", "ERAGON", "ESTOMAGO", "EVITA", "FAILAN", "FARGO", "FRACTURE",
            "FURTIVOS", "GAMER", "GENOVA", "GHANDI", "GHOST", "GIGLI", "GOOD",
            "GOMORRA", "GORGO", "GREASE", "GREMLINS", "HACHIKO", "HAMLET", "HANCOCK",
            "HANNIBAL", "HAPPY", "HERO", "HITCH", "HOME", "HOSTEL", "JARHEAD",
            "JULIA", "JUMPER", "JUNIOR", "JUNO", "JVCD", "KINSEY", "KUNDUM",
            "LANTANA", "LOOPER", "MACHETE", "MAMA", "MATILDA", "MATRIX", "MEMENTO",
            "MONSTER", "MOON", "MUNICH", "NAUFRAGO", "NIAGARA", "OLIVER", "ORIGEN",
            "OTHELLO", "PAPILLON", "PLACIDO", "PLATOON", "PELOTON", "POSTAL",
            "PRECIOUS", "PSICOSIS", "PUSH", "RADIO", "RAMBO", "RANGO", "REDS",
            "REC", "REFLEJOS", "ROBOCOP", "ROCKY", "SAW", "SCARFACE", "SCOOP",
            "SEVEN", "SHINE", "SHREK", "SICKO", "SINISTER", "SKYFALL", "SPEED",
            "SPLASH", "STARGATE", "STONE", "SUNSHINE", "SUPERMAN", "SURCOS",
            "SUSPENSE", "SYRIANA", "TANGLED", "TAXI", "TEKKEN", "TESIS", "TIBURON",
            "TIDELAND", "TIERRA", "TIME", "TITANIC", "TOOTSIE", "TRISTANA", "TRON",
            "TROYA", "VACAS", "VALKIRIA", "VERTIGO", "WARRIOR", "XMEN", "XXY", "ZODIAC"]

        dicTemas = {
            "un animal": ANIMALES,
            "un color": COLORES,
            "una flor": FLORES,
            "un deporte o juego": DEPORTES,
            "un alimento o plato cocinado": ALIMENTOS,
            "un elemento químico": QUIMICOS,
            "un vehículo o medio de transporte": VEHICULOS,
            "una parte del cuerpo u órgano interno": CUERPO,
            "una prenda de vestir o complemento": PRENDAS,
            "una profesión u oficio": OFICIOS,
            "un número": NUMEROS,
            "una ciudad": CIUDADES,
            "el título de una película": PELICULAS}

        # Seleccionar palabra
        palabras = []
        for key in dicTemas:
            for parole in dicTemas[key]:
                palabras.append(parole)
        self.palabra = choice(palabras)

        # Obtener pista
        self.pista = "un... mejor no, esfuérzate un poco más."
        for key, tema in dicTemas.items():
            for parole in tema:
                if parole == self.palabra:
                    self.pista = key

        # Ocultar palabra
        self.secreta = len(self.palabra) * "_"
        self.lista = list(self.secreta)

        self.fallos = 0

    def checkLetra(self, letra):
        if letra not in self.palabra:
            return False
        index = 0
        while index < len(self.palabra):
            if self.palabra[index] == letra:
                self.lista[index] = letra
            index += 1
        return self.lista

    def sumaError(self):
        self.fallos += 1
        return self.fallos

    def checkVictoria(self, listaCheck):
        if self.palabra == ("".join(listaCheck)):
            return True
        return False

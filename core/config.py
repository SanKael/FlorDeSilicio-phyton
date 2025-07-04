# config.py – Configuración global del proyecto

from colorama import Fore, Style

DEBUG = False  # Cambia a False si no quieres ver info extra
RESET = "\033[0m"
TIPOS_VALIDOS = ["fuego", "agua", "tierra", "aire", "luz", "oscuridad"]
TIPO_COLORES = {
    "fuego": "\033[91m",       # rojo
    "agua": "\033[94m",        # azul
    "tierra": "\033[92m",      # verde
    "aire": "\033[96m",        # cian
    "luz": "\033[93m",         # amarillo
    "oscuridad": "\033[95m",   # magenta
}

# Ruta al archivo de datos
DATA_PATH = "data/criaturas.json"

# Tipos válidos de criaturas
TIPOS_VALIDOS = [
    "fuego", "agua", "tierra", "aire",
    "luz", "oscuridad", "eléctrico", "hielo",
    "veneno", "fantasma"
]

# Colores temáticos por tipo
TIPO_COLORES = {
    "fuego": Fore.RED,
    "agua": Fore.BLUE,
    "tierra": Fore.YELLOW,
    "aire": Fore.CYAN,
    "luz": Fore.WHITE,
    "oscuridad": Fore.MAGENTA,
    "eléctrico": Fore.LIGHTYELLOW_EX,
    "hielo": Fore.LIGHTCYAN_EX,
    "veneno": Fore.GREEN,
    "fantasma": Fore.LIGHTMAGENTA_EX
}

# Reset de estilo de color
RESET = Style.RESET_ALL

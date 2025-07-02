# config.py – Configuración global del proyecto

from colorama import Fore, Style

# Modo debug (True para mostrar info extra, False para ocultarla)
DEBUG = True

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

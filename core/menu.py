# core/menu.py
from colorama import Fore
from core.config import RESET

def mostrar_menu():
    print(Fore.LIGHTMAGENTA_EX + "\n🌟 MENÚ PRINCIPAL – Criaturas Mágicas" + RESET)
    print(Fore.YELLOW + "1. Añadir criatura" + RESET)
    print(Fore.CYAN + "2. Buscar criatura" + RESET)
    print(Fore.RED + "3. Eliminar criatura" + RESET)
    print(Fore.GREEN + "4. Mostrar todas" + RESET)
    print(Fore.BLUE + "5. Mostrar por tipo" + RESET)
    print(Fore.MAGENTA + "6. Guardar" + RESET)
    print(Fore.LIGHTWHITE_EX + "7. Salir" + RESET)


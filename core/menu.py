from colorama import Fore, Style

def mostrar_menu():
    print(Fore.LIGHTMAGENTA_EX + "\n╔════════════════════════════╗")
    print("║    " + Fore.YELLOW + "🧙 MENÚ DE CRIATURAS" + Fore.LIGHTMAGENTA_EX + "    ║")
    print("╚════════════════════════════╝" + Style.RESET_ALL)

    print(Fore.CYAN + "1." + Fore.WHITE + " Añadir criatura")
    print(Fore.CYAN + "2." + Fore.WHITE + " Buscar criatura")
    print(Fore.CYAN + "3." + Fore.LIGHTRED_EX + " Eliminar criatura")  # <- solo el texto va en rojo suave
    print(Fore.CYAN + "4." + Fore.WHITE + " Mostrar todas")
    print(Fore.CYAN + "5." + Fore.WHITE + " Mostrar por tipo")
    print(Fore.CYAN + "6." + Fore.WHITE + " Editar criatura")
    print(Fore.CYAN + "7." + Fore.WHITE + " Salir" + Style.RESET_ALL)

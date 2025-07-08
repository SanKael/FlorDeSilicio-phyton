from colorama import Fore, Style, init
from modules.utils import (
    añadir_criatura,
    buscar_criatura,
    eliminar_criatura,
    mostrar_todas,
    mostrar_por_tipo,
    editar_criatura,
)
from core.file_handler import guardar_en_json, cargar_desde_json, guardar_en_txt, cargar_desde_txt
from core.menu import mostrar_menu
from core.config import DEBUG, RESET
import os

DRAMATIC_MODE = False  # Cambia a False para desactivarlo

from modules.utils import cuenta_atras_dramatica

if DRAMATIC_MODE:
    cuenta_atras_dramatica()

init(autoreset=True)

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar():
    input(Fore.LIGHTBLACK_EX + "\nPulsa Enter para continuar..." + RESET)

# Formato de guardado
modo_actual = input("¿Qué formato deseas usar? (txt/json): ").strip().lower()
if modo_actual not in ("txt", "json"):
    print("Formato no válido. Se usará 'json' por defecto.")
    modo_actual = "json"

# Cargar criaturas
criaturas = cargar_desde_json() if modo_actual == "json" else cargar_desde_txt()

# Bucle principal
while True:
    limpiar_pantalla()

    if DEBUG:
        print(Fore.LIGHTBLACK_EX + f"\n[DEBUG] Modo: {modo_actual} | Criaturas cargadas: {len(criaturas)}")
        for c in criaturas:
            print(f"- {c['nombre']} (nivel {c['nivel']}, tipo {c['tipo']}, etiquetas: {', '.join(c.get('etiquetas', []))})")

    mostrar_menu()
    opcion = input(Fore.LIGHTGREEN_EX + "\n👉 Elige una opción (1-7): " + Style.RESET_ALL).strip()

    if opcion == "1":
        print("👉 Añadir criatura")
        añadir_criatura(criaturas)
        pausar()
    elif opcion == "2":
        print("🔍 Buscar criatura")
        buscar_criatura(criaturas)
        pausar()
    elif opcion == "3":
        print("🗑️ Eliminar criatura")
        eliminar_criatura(criaturas)
        pausar()
    elif opcion == "4":
        print("📜 Mostrar todas")
        mostrar_todas(criaturas)
        pausar()
    elif opcion == "5":
        print("📂 Mostrar por tipo")
        mostrar_por_tipo(criaturas)
        pausar()
    elif opcion == "6":
        print("🛠️ Editar criatura")
        editar_criatura(criaturas)
        pausar()
    elif opcion == "7":
        print("💾 Guardando antes de salir...")
        if modo_actual == "json":
            guardar_en_json(criaturas)
        else:
            guardar_en_txt(criaturas)
        print(Fore.CYAN + "👋 ¡Hasta la próxima!")
        break
    else:
        print(Fore.RED + "⚠️ Opción no válida.")
        pausar()

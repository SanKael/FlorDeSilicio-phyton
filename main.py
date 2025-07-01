from colorama import Fore, init
from modules.utils import (
    añadir_criatura,
    buscar_criatura,
    eliminar_criatura,
    mostrar_todas,
    mostrar_por_tipo
)
from core.menu_actions import ejecutar_opcion
from core.file_handler import guardar_en_json, cargar_desde_json, guardar_en_txt, cargar_desde_txt
from core.menu import mostrar_menu

init(autoreset=True)

# 🐞 Activar o desactivar modo debug
DEBUG = False

def debug_print(msg):
    if DEBUG:
        print(Fore.MAGENTA + "[DEBUG] " + str(msg))

# Preguntar al usuario el formato
modo_actual = input("¿Qué formato deseas usar? (txt/json): ").strip().lower()
if modo_actual not in ("txt", "json"):
    print("Formato no válido. Se usará 'json' por defecto.")
    modo_actual = "json"

# Cargar datos según el modo
if modo_actual == "json":
    criaturas = cargar_desde_json()
else:
    criaturas = cargar_desde_txt()

debug_print(f"Modo de guardado seleccionado: {modo_actual}")  # 🐞 DEBUG
debug_print(f"Criaturas cargadas: {criaturas}")  # 🐞 DEBUG

while True:
    mostrar_menu()
    opcion = input("Elige una opción (1-7): ").strip()

    if opcion == "1":
        print("👉 Añadir criatura")
        añadir_criatura(criaturas)
    elif opcion == "2":
        print("🔍 Buscar criatura")
        buscar_criatura(criaturas)
    elif opcion == "3":
        print("🗑️ Eliminar criatura")
        eliminar_criatura(criaturas)
    elif opcion == "4":
        print("📜 Mostrar todas")
        mostrar_todas(criaturas)
    elif opcion == "5":
        print("📂 Mostrar por tipo")
        mostrar_por_tipo(criaturas)       # NUEVA FUNCIÓN
    elif opcion == "6":
        print("💾 Guardando...")
        guardar(criaturas, modo_actual)
    elif opcion == "7":
        guardar(criaturas, modo_actual)
        print(Fore.CYAN + "👋 Datos guardados. Saliendo del programa. ¡Hasta la próxima!")
        break
    else:
        print(Fore.RED + "⚠️ Opción no válida.")


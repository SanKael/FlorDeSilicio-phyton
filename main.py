from colorama import Fore, init
from modules.utils import (
    añadir_criatura,
    buscar_criatura,
    eliminar_criatura,
    mostrar_todas,
    mostrar_por_tipo
)
from core.menu_actions import ejecutar_opcion, guardar_datos
from core.file_handler import guardar_en_json, cargar_desde_json, guardar_en_txt, cargar_desde_txt
from core.menu import mostrar_menu
from core.config import DEBUG, DATA_PATH, TIPOS_VALIDOS, TIPO_COLORES, RESET
import os

init(autoreset=True)

# 🐞 Activar o desactivar modo debug
DEBUG = False

# Función para limpiar pantalla
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

# Función para pausar entre acciones
def pausar():
    input(Fore.LIGHTBLACK_EX + "\nPulsa Enter para continuar..." + RESET)

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

while True:
    limpiar_pantalla()
    mostrar_menu()
    opcion = input("Elige una opción (1-7): ").strip()

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
        print("💾 Guardando...")
        guardar_datos(criaturas, modo_actual)
        print(Fore.GREEN + "✅ Datos guardados correctamente.")
        pausar()
    elif opcion == "7":
        guardar_datos(criaturas, modo_actual)
        print(Fore.CYAN + "👋 Datos guardados. Saliendo del programa. ¡Hasta la próxima!")
        break
    else:
        print(Fore.RED + "⚠️ Opción no válida.")
        pausar()

from colorama import Fore, Style, init
import json
from modules.utils import (
    añadir_criatura,
    buscar_criatura,
    eliminar_criatura,
    mostrar_todas
)
from core.file_handler import guardar_en_json, cargar_desde_json

init(autoreset=True)

def mostrar_menu():
    print(Fore.YELLOW + Style.BRIGHT + "\n🌟 Menú de opciones:")
    print(Fore.CYAN + "1. Añadir criatura")
    print("2. Buscar criatura")
    print("3. Eliminar criatura")
    print("4. Mostrar todas")
    print("5. Guardar en archivo JSON")
    print("6. Salir")

criaturas = []

# Carga automática
cargar_desde_json(criaturas)

while True:
    mostrar_menu()
    opcion = input("Elige una opción (1-6): ").strip()

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
        print("💾 Guardando en JSON")
        guardar_en_json(criaturas)
    elif opcion == "6":
        guardar_en_json(criaturas)
        print(Fore.CYAN + "👋 Datos guardados. Saliendo del programa. ¡Hasta la próxima!")
        break
    else:
        print(Fore.RED + "⚠️ Opción no válida.")

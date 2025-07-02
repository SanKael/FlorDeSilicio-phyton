# core/menu_actions.py

from colorama import Fore
from modules.utils import (
    añadir_criatura,
    buscar_criatura,
    eliminar_criatura,
    mostrar_todas,
    mostrar_por_tipo
)
from core.file_handler import guardar_en_json, guardar_en_txt

def ejecutar_opcion(opcion, criaturas, modo):
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
        guardar(criaturas, modo)
        print(Fore.CYAN + "👋 Datos guardados. Saliendo del programa. ¡Hasta la próxima!")
        exit()
    else:
        print(Fore.RED + "⚠️ Opción no válida.")

def guardar(criaturas, modo):
    if modo == "json":
        guardar_en_json(criaturas)
    elif modo == "txt":
        guardar_en_txt(criaturas)
    else:
        print(Fore.RED + "⚠️ Modo de guardado no reconocido.")

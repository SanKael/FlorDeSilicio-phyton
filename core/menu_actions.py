from modules.utils import (
    añadir_criatura,
    buscar_criatura,
    eliminar_criatura,
    mostrar_todas
)
from core.file_handler import guardar
from colorama import Fore

def ejecutar_opcion(opcion, criaturas):
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
        exit()
    else:
        print(Fore.RED + "⚠️ Opción no válida.")

from colorama import Fore, Style, init
from modules.utils import (
    añadir_criatura,
    buscar_criatura,
    eliminar_criatura,
    mostrar_todas,
    mostrar_por_tipo,
    editar_criatura,
    cuenta_atras_dramatica,
    validar_opcion_menu,  # ✅ Nueva función para validar la opción del menú
)
from core.file_handler import guardar_en_json, cargar_desde_json, guardar_en_txt, cargar_desde_txt
from core.menu import mostrar_menu
from core.config import DEBUG, RESET
import os

# 🎬 Activar cuenta atrás dramática si está habilitada
DRAMATIC_MODE = False  # Cambia a True si quieres activar la cuenta atrás

if DRAMATIC_MODE:
    cuenta_atras_dramatica()

# 🎨 Inicializa colorama para estilos en consola
init(autoreset=True)

# 🧼 Limpia la pantalla según el sistema operativo
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

# ⏸️ Pausa el programa hasta que el usuario pulse Enter
def pausar():
    input(Fore.LIGHTBLACK_EX + "\nPulsa Enter para continuar..." + RESET)

# 💾 Pregunta por el formato de guardado (txt/json)
modo_actual = input("¿Qué formato deseas usar? (txt/json): ").strip().lower()
if modo_actual not in ("txt", "json"):
    print("Formato no válido. Se usará 'json' por defecto.")
    modo_actual = "json"

# 📂 Carga inicial de criaturas desde archivo
criaturas = cargar_desde_json() if modo_actual == "json" else cargar_desde_txt()

# 🔁 Bucle principal del programa
while True:
    limpiar_pantalla()

    # 🐞 Modo depuración (si está activado)
    if DEBUG:
        print(Fore.LIGHTBLACK_EX + f"\n[DEBUG] Modo: {modo_actual} | Criaturas cargadas: {len(criaturas)}")
        for c in criaturas:
            print(f"- {c['nombre']} (nivel {c['nivel']}, tipo {c['tipo']}, etiquetas: {', '.join(c.get('etiquetas', []))})")

    mostrar_menu()

    # ✅ Validar opción de menú con función personalizada
    while True:
        entrada = input(Fore.LIGHTGREEN_EX + "\n👉 Elige una opción (1-7): " + Style.RESET_ALL)
        opcion = validar_opcion_menu(entrada, range(1, 8))  # solo acepta valores del 1 al 7
        if opcion is not None:
            break

    # 📦 Lógica de opciones según lo validado
    if opcion == 1:
        print("👉 Añadir criatura")
        añadir_criatura(criaturas)
        pausar()
    elif opcion == 2:
        print("🔍 Buscar criatura")
        buscar_criatura(criaturas)
        pausar()
    elif opcion == 3:
        print("🗑️ Eliminar criatura")
        eliminar_criatura(criaturas)
        pausar()
    elif opcion == 4:
        print("📜 Mostrar todas")
        mostrar_todas(criaturas)
        pausar()
    elif opcion == 5:
        print("📂 Mostrar por tipo")
        mostrar_por_tipo(criaturas)
        pausar()
    elif opcion == 6:
        print("🛠️ Editar criatura")
        editar_criatura(criaturas)
        pausar()
    elif opcion == 7:
        print("💾 Guardando antes de salir...")
        if modo_actual == "json":
            guardar_en_json(criaturas)
        else:
            guardar_en_txt(criaturas)
        print(Fore.CYAN + "👋 ¡Hasta la próxima!")
        break

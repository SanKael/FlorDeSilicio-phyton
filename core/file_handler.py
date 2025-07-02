# core/file_handler.py

import json
from colorama import Fore
from core.config import DATA_PATH, RESET

def guardar_en_json(lista, archivo=DATA_PATH):
    try:
        with open(archivo, "w", encoding="utf-8") as f:
            json.dump(lista, f, indent=2, ensure_ascii=False)
        print(Fore.GREEN + "💾 Guardado en JSON exitoso." + RESET)
    except Exception as e:
        print(Fore.RED + f"❌ Error al guardar en JSON: {e}" + RESET)

def cargar_desde_json(archivo=DATA_PATH):
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            lista = json.load(f)
        print(Fore.CYAN + "📂 Datos cargados desde JSON." + RESET)
        return lista
    except FileNotFoundError:
        print(Fore.YELLOW + "⚠️ Archivo JSON no encontrado." + RESET)
        return []
    except Exception as e:
        print(Fore.RED + f"❌ Error al cargar JSON: {e}" + RESET)
        return []

def guardar_en_txt(lista, archivo="data/criaturas.txt"):
    try:
        with open(archivo, "w", encoding="utf-8") as f:
            for criatura in lista:
                f.write(f"{criatura['nombre']},{criatura['tipo']},{criatura['nivel']}\n")
        print(Fore.GREEN + "💾 Guardado en TXT exitoso." + RESET)
    except Exception as e:
        print(Fore.RED + f"❌ Error al guardar en TXT: {e}" + RESET)

def cargar_desde_txt(archivo="data/criaturas.txt"):
    lista = []
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            for linea in f:
                partes = linea.strip().split(",")
                if len(partes) != 3:
                    continue
                nombre, tipo, nivel = partes
                if nivel.isdigit():
                    lista.append({
                        "nombre": nombre.strip().lower(),
                        "tipo": tipo.strip().lower(),
                        "nivel": int(nivel)
                    })
        print(Fore.CYAN + "📂 Datos cargados desde TXT." + RESET)
    except FileNotFoundError:
        print(Fore.YELLOW + "⚠️ Archivo TXT no encontrado." + RESET)
    return lista

# Funciones de alto nivel
def cargar(formato="json"):
    if formato == "txt":
        return cargar_desde_txt()
    elif formato == "json":
        return cargar_desde_json()
    else:
        print(Fore.RED + f"⚠️ Formato '{formato}' no reconocido. Usando JSON por defecto." + RESET)
        return cargar_desde_json()

def guardar(lista, formato="json"):
    if formato == "txt":
        guardar_en_txt(lista)
    elif formato == "json":
        guardar_en_json(lista)
    else:
        print(Fore.RED + f"⚠️ Formato '{formato}' no reconocido. Guardando en JSON por defecto." + RESET)
        guardar_en_json(lista)

# core/file_handler.py
import json
from colorama import Fore

def guardar_en_json(lista, archivo="data/criaturas.json"):
    try:
        with open(archivo, "w", encoding="utf-8") as f:
            json.dump(lista, f, indent=2, ensure_ascii=False)
        print(Fore.GREEN + "💾 Guardado en JSON exitoso.")
    except Exception as e:
        print(Fore.RED + f"❌ Error al guardar en JSON: {e}")

def cargar_desde_json(archivo="data/criaturas.json"):
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            lista = json.load(f)
        print(Fore.CYAN + "📂 Datos cargados desde JSON.")
        return lista
    except FileNotFoundError:
        print(Fore.YELLOW + "⚠️ Archivo JSON no encontrado.")
        return []
    except Exception as e:
        print(Fore.RED + f"❌ Error al cargar JSON: {e}")
        return []

def guardar_en_txt(lista, archivo="data/criaturas.txt"):
    try:
        with open(archivo, "w", encoding="utf-8") as f:
            for criatura in lista:
                f.write(f"{criatura['nombre']},{criatura['tipo']},{criatura['nivel']}\n")
        print(Fore.GREEN + "💾 Guardado en TXT exitoso.")
    except Exception as e:
        print(Fore.RED + f"❌ Error al guardar en TXT: {e}")

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
        print(Fore.CYAN + "📂 Datos cargados desde TXT.")
    except FileNotFoundError:
        print(Fore.YELLOW + "⚠️ Archivo TXT no encontrado.")
    return lista

# Funciones de alto nivel
def cargar(formato="json"):
    if formato == "txt":
        return cargar_desde_txt()
    return cargar_desde_json()

def guardar(lista, formato="json"):
    if formato == "txt":
        guardar_en_txt(lista)
    else:
        guardar_en_json(lista)


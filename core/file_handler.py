import json
from colorama import Fore

def guardar_en_json(lista, archivo="data/criaturas.json"):
    try:
        with open(archivo, "w", encoding="utf-8") as f:
            json.dump(lista, f, indent=4, ensure_ascii=False)
        print(Fore.GREEN + "💾 Datos guardados en JSON correctamente.")
    except Exception as e:
        print(Fore.RED + f"❌ Error al guardar en JSON: {e}")

def cargar_desde_json(lista, archivo="data/criaturas.json"):
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            datos = json.load(f)
            for criatura in datos:
                if not any(c["nombre"] == criatura["nombre"] for c in lista):
                    lista.append(criatura)
        print(Fore.GREEN + "📂 Datos cargados desde JSON correctamente.")
    except FileNotFoundError:
        print(Fore.YELLOW + "⚠️ No se encontró el archivo JSON. Aún no hay datos guardados.")
    except json.JSONDecodeError:
        print(Fore.RED + "❌ El archivo JSON está corrupto o malformado.")

import json
from colorama import Fore, Style

def añadir_criatura(lista):
    try:
        nombre = input("Nombre de la criatura: ").strip().lower()
        if not nombre:
            raise ValueError("El nombre no puede estar vacío.")
        if any(c["nombre"] == nombre for c in lista):
            print(Fore.RED + "⚠️ Ya existe una criatura con ese nombre.")
            return

        tipo = input("Tipo de criatura: ").strip().lower()
        if not tipo:
            raise ValueError("El tipo no puede estar vacío.")

        nivel = input("Nivel (entero positivo): ").strip()
        if not nivel.isdigit() or int(nivel) <= 0:
            raise ValueError("El nivel debe ser un número entero positivo.")

        criatura = {
            "nombre": nombre,
            "tipo": tipo,
            "nivel": int(nivel)
        }
        lista.append(criatura)
        print(Fore.GREEN + f"✅ Criatura '{nombre}' añadida con éxito.")
    except ValueError as ve:
        print(Fore.RED + f"Error: {ve}")


def buscar_criatura(lista):
    nombre = input("🔎 Nombre de la criatura a buscar: ").strip().lower()
    for criatura in lista:
        if criatura["nombre"] == nombre:
            print(Fore.BLUE + "\n📌 Criatura encontrada:")
            print(f"- Nombre: {criatura['nombre'].capitalize()}")
            print(f"- Tipo: {criatura['tipo'].capitalize()}")
            print(f"- Nivel: {criatura['nivel']}")
            return
    print(Fore.RED + "❌ No se encontró ninguna criatura con ese nombre.")


def eliminar_criatura(lista):
    nombre = input("🗑️ Nombre de la criatura a eliminar: ").strip().lower()
    for criatura in lista:
        if criatura["nombre"] == nombre:
            print(f"⚠️ ¿Estás seguro de que quieres eliminar '{nombre}'?")
            confirmacion = input("Escribe 'sí' para confirmar: ").strip().lower()
            if confirmacion == "sí":
                lista.remove(criatura)
                print(Fore.GREEN + f"✅ '{nombre}' ha sido eliminada.")
            else:
                print(Fore.YELLOW + "❎ Eliminación cancelada.")
            return
    print(Fore.RED + "❌ No se encontró ninguna criatura con ese nombre.")


def mostrar_todas(lista):
    if not lista:
        print(Fore.YELLOW + "🌫️ No hay criaturas registradas.")
    else:
        print(Fore.MAGENTA + "\n📜 Tu colección de criaturas:")
        for i, criatura in enumerate(lista, 1):
            nombre = criatura['nombre']
            tipo = criatura['tipo']
            nivel = criatura['nivel']
            color = obtener_color_por_tipo(tipo)

            print(color + f"{i}. {nombre.capitalize():20} | Tipo: {tipo.capitalize():15} | Nivel: {nivel}")


# 🎨 Paleta de colores por tipo
def obtener_color_por_tipo(tipo):
    tipo = tipo.lower()
    if tipo == "fuego":
        return Fore.RED
    elif tipo == "agua":
        return Fore.CYAN
    elif tipo == "sombra":
        return Fore.MAGENTA
    elif tipo == "tierra":
        return Fore.YELLOW
    elif tipo == "legendaria":
        return Fore.LIGHTWHITE_EX + Style.BRIGHT
    else:
        return Fore.WHITE
def mostrar_por_tipo(lista):
    if not lista:
        print(Fore.YELLOW + "🌫️ No hay criaturas registradas.")
        return

    tipos = set(c["tipo"] for c in lista)
    print(Fore.CYAN + "🔎 Tipos disponibles:")
    for tipo in tipos:
        print(f"- {tipo.capitalize()}")

    tipo_buscar = input("¿Qué tipo quieres mostrar?: ").strip().lower()
    criaturas_filtradas = [c for c in lista if c["tipo"] == tipo_buscar]

    if criaturas_filtradas:
        print(Fore.MAGENTA + f"\n📜 Criaturas del tipo '{tipo_buscar.capitalize()}':")
        for i, criatura in enumerate(criaturas_filtradas, 1):
            print(Fore.CYAN + f"{i}. {criatura['nombre'].capitalize()} (Nivel {criatura['nivel']})")
    else:
        print(Fore.RED + "❌ No se encontraron criaturas de ese tipo.")


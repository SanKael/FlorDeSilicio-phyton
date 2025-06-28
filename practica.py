from colorama import Fore, Style, init
import json

init(autoreset=True)

criaturas = []

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

            if nombre == "sofía la luminosa":
                color = Fore.LIGHTWHITE_EX + Style.BRIGHT
            elif nombre == "pepino astral":
                color = Fore.GREEN + Style.BRIGHT
            else:
                color = Fore.CYAN

            print(color + f"{i}. {nombre.capitalize():20} | Tipo: {tipo.capitalize():15} | Nivel: {nivel}")


def cargar_desde_json(lista, archivo="criaturas.json"):
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            datos = json.load(f)
            for criatura in datos:
                if not any(c["nombre"] == criatura["nombre"] for c in lista):
                    lista.append(criatura)
        print(Fore.GREEN + "✅ Datos cargados desde JSON correctamente.")
    except FileNotFoundError:
        print(Fore.YELLOW + "⚠️ Archivo JSON no encontrado.")
    except json.JSONDecodeError:
        print(Fore.RED + "❌ Error de formato en el JSON.")


def guardar_en_json(lista, archivo="criaturas.json"):
    try:
        with open(archivo, "w", encoding="utf-8") as f:
            json.dump(lista, f, indent=4, ensure_ascii=False)
        print(Fore.GREEN + "💾 Datos guardados en JSON correctamente.")
    except Exception as e:
        print(Fore.RED + f"❌ Error al guardar en JSON: {e}")


def mostrar_menu():
    print(Fore.YELLOW + Style.BRIGHT + "\n🌟 Menú de opciones:")
    print(Fore.CYAN + "1. Añadir criatura")
    print("2. Buscar criatura")
    print("3. Eliminar criatura")
    print("4. Mostrar todas")
    print("5. Guardar en archivo JSON")
    print("6. Salir")


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

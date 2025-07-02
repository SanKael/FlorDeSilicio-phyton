from colorama import Fore
from core.config import TIPO_COLORES, RESET, TIPOS_VALIDOS

def añadir_criatura(lista):
    nombre = input("Nombre de la criatura: ").strip()
    tipo = input("Tipo de la criatura: ").strip().lower()

    if tipo not in TIPOS_VALIDOS:
        print(Fore.RED + f"❌ Tipo no válido. Tipos permitidos: {', '.join(TIPOS_VALIDOS)}")
        return

    try:
        nivel = int(input("Nivel de la criatura: "))
    except ValueError:
        print(Fore.RED + "⚠️ El nivel debe ser un número entero.")
        return

    criatura = {"nombre": nombre, "tipo": tipo, "nivel": nivel}
    lista.append(criatura)
    print(Fore.GREEN + f"✅ Criatura '{nombre}' añadida correctamente.")

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
        return

    print(Fore.LIGHTMAGENTA_EX + "\n📜 Lista completa de criaturas:" + RESET)
    for i, criatura in enumerate(lista, 1):
        tipo = criatura["tipo"]
        color = TIPO_COLORES.get(tipo, Fore.LIGHTWHITE_EX)
        print(f"{color}{i}. {criatura['nombre'].capitalize()} (Nivel {criatura['nivel']}) - Tipo: {tipo.capitalize()}{RESET}")

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
        color_tipo = TIPO_COLORES.get(tipo_buscar, Fore.WHITE)

        for i, criatura in enumerate(criaturas_filtradas, 1):
            print(
                f"{color_tipo}{i}. {criatura['nombre'].capitalize()} "
                f"(Nivel {criatura['nivel']}){RESET}"
            )
    else:
        print(Fore.RED + "❌ No se encontraron criaturas de ese tipo.")

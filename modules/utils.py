from colorama import Fore
from core.config import TIPO_COLORES, RESET, TIPOS_VALIDOS, DEBUG

def añadir_criatura(lista):
    # Nombre (no repetido)
    while True:
        nombre = input("Nombre de la criatura: ").strip()
        if not nombre:
            print(Fore.RED + "❌ El nombre no puede estar vacío.")
        elif any(c["nombre"].lower() == nombre.lower() for c in lista):
            print(Fore.RED + f"❌ Ya existe una criatura llamada '{nombre}'. Usa otro nombre.")
        else:
            break

    # Tipo (debe estar en TIPOS_VALIDOS)
    while True:
        tipo = input("Tipo de la criatura: ").strip().lower()
        if tipo not in TIPOS_VALIDOS:
            print(Fore.RED + f"❌ Tipo no válido. Tipos permitidos: {', '.join(TIPOS_VALIDOS)}")
        else:
            break

    # Nivel (entre 1 y 100)
    while True:
        try:
            nivel = int(input("Nivel de la criatura (1–100): "))
            if 1 <= nivel <= 100:
                break
            else:
                print(Fore.RED + "⚠️ El nivel debe estar entre 1 y 100.")
        except ValueError:
            print(Fore.RED + "⚠️ El nivel debe ser un número.")

    # Etiquetas opcionales
    etiquetas_input = input("Etiquetas (separadas por comas, opcional): ").strip()
    etiquetas = [e.strip().lower() for e in etiquetas_input.split(",") if e.strip()] if etiquetas_input else []

    # Crear criatura
    criatura = {
        "nombre": nombre,
        "tipo": tipo,
        "nivel": nivel,
        "etiquetas": etiquetas
    }

    lista.append(criatura)
    print(Fore.GREEN + f"✅ Criatura '{nombre}' añadida correctamente con {len(etiquetas)} etiqueta(s).")

def buscar_criatura(lista):
    if not lista:
        print(Fore.YELLOW + "🌫️ No hay criaturas registradas para buscar.")
        return

    termino = input("🔎 Escribe el nombre o parte del nombre de la criatura: ").strip().lower()
    resultados = []

    for criatura in lista:
        if termino in criatura["nombre"].lower():
            resultados.append(criatura)

    if resultados:
        print(Fore.CYAN + f"\n🔍 Resultados de búsqueda para '{termino}':")
        for i, criatura in enumerate(resultados, 1):
            tipo = criatura["tipo"]
            color = TIPO_COLORES.get(tipo, Fore.LIGHTWHITE_EX)
            print(f"{color}{i}. {criatura['nombre'].capitalize()} (Nivel {criatura['nivel']}) - Tipo: {tipo.capitalize()}{RESET}")
            if criatura.get("etiquetas"):
                print(Fore.LIGHTBLACK_EX + f"   🏷️ Etiquetas: {', '.join(criatura['etiquetas'])}" + RESET)
    else:
        print(Fore.RED + f"❌ No se encontraron criaturas que coincidan con '{termino}'.")

def eliminar_criatura(lista):
    nombre = input("Nombre de la criatura a eliminar: ").strip().lower()

    for criatura in lista:
        if criatura["nombre"].lower() == nombre:
            confirmacion = input(Fore.RED + f"⚠️ ¿Estás seguro de que quieres eliminar '{criatura['nombre']}'? (s/n): " + RESET).strip().lower()
            if confirmacion == "s":
                lista.remove(criatura)
                print(Fore.GREEN + f"✅ Criatura '{criatura['nombre']}' eliminada con éxito." + RESET)
            else:
                print(Fore.LIGHTBLACK_EX + "❎ Operación cancelada." + RESET)
            return

    print(Fore.YELLOW + f"🧐 No se encontró ninguna criatura con el nombre '{nombre}'." + RESET)

def mostrar_todas(lista):
    if not lista:
        print(Fore.YELLOW + "🌫️ No hay criaturas registradas.")
        return

    print(Fore.LIGHTMAGENTA_EX + "\n📜 Lista completa de criaturas:" + RESET)
    for i, criatura in enumerate(lista, 1):
        tipo = criatura["tipo"]
        color = TIPO_COLORES.get(tipo, Fore.LIGHTWHITE_EX)
        print(f"{color}{i}. {criatura['nombre'].capitalize()} (Nivel {criatura['nivel']}) - Tipo: {tipo.capitalize()}{RESET}")
        if criatura.get("etiquetas"):
            print(Fore.LIGHTBLACK_EX + f"   🏷️ Etiquetas: {', '.join(criatura['etiquetas'])}" + RESET)
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

def editar_criatura(lista):
    if not lista:
        print(Fore.YELLOW + "🌫️ No hay criaturas para editar.")
        return

    mostrar_todas(lista)

    try:
        index = int(input("Número de la criatura que quieres editar: ")) - 1
        if index < 0 or index >= len(lista):
            print(Fore.RED + "❌ Número fuera de rango.")
            return
    except ValueError:
        print(Fore.RED + "❌ Debes introducir un número válido.")
        return

    criatura = lista[index]
    print(Fore.LIGHTCYAN_EX + f"\nEditando a {criatura['nombre'].capitalize()}:" + RESET)

    nuevo_nombre = input(f"Nuevo nombre (Enter para mantener '{criatura['nombre']}'): ").strip()
    if nuevo_nombre:
        criatura['nombre'] = nuevo_nombre

    nuevo_tipo = input(f"Nuevo tipo (Enter para mantener '{criatura['tipo']}'): ").strip().lower()
    if nuevo_tipo:
        if nuevo_tipo in TIPOS_VALIDOS:
            criatura['tipo'] = nuevo_tipo
        else:
            print(Fore.RED + f"⚠️ Tipo no válido. Se mantiene el actual: {criatura['tipo']}")

    try:
        nuevo_nivel = input(f"Nuevo nivel (1–100, Enter para mantener {criatura['nivel']}): ").strip()
        if nuevo_nivel:
            nivel_int = int(nuevo_nivel)
            if 1 <= nivel_int <= 100:
                criatura['nivel'] = nivel_int
            else:
                print(Fore.RED + "⚠️ Nivel fuera de rango. Se mantiene el actual.")
    except ValueError:
        print(Fore.RED + "⚠️ Nivel inválido. Se mantiene el actual.")

    nuevas_etiquetas = input("Nuevas etiquetas (coma separadas, Enter para mantener las actuales): ").strip()
    if nuevas_etiquetas:
        criatura['etiquetas'] = [e.strip().lower() for e in nuevas_etiquetas.split(",") if e.strip()]

    print(Fore.GREEN + "✅ Criatura editada correctamente.")

from colorama import Fore, Style # Importa Fore y Style de colorama
from core.config import TIPO_COLORES, RESET, TIPOS_VALIDOS, DEBUG
import time
# 🔧 Función universal para limpiar entradas de texto
def limpiar_input(texto, formato="lower"):
    texto = texto.strip()
    if formato == "lower":
        return texto.lower()
    elif formato == "capitalize":
        return texto.capitalize()
    elif formato == "title":
        return texto.title()
    else:
        return texto
# 🔧 Función para validar si el texto contiene al menos un carácter alfanumérico
def es_input_valido(texto):
    texto = texto.strip()
    return any(c.isalnum() for c in texto)
# 🔧 Función para validar el nivel de la criatura
def validar_nivel(input_str):
    """
    Recibe una cadena, intenta convertirla a entero y valida que esté entre 1 y 100.
    Devuelve el número si es válido, o None si no lo es.
    """
    try:
        nivel = int(input_str.strip())
        if 1 <= nivel <= 100:
            return nivel
        else:
            print(Fore.RED + "⚠️ El nivel debe estar entre 1 y 100.")
    except ValueError:
        print(Fore.RED + "⚠️ Debes escribir un número válido.")
    return None
# 🔧 Función para validar opciones del menú
def validar_opcion_menu(input_str, opciones_validas):
    try:
        opcion = int(input_str.strip())
        if opcion in opciones_validas:
            return opcion
        else:
            print(Fore.RED + f"⚠️ Debes elegir una opción entre {min(opciones_validas)} y {max(opciones_validas)}.")
    except ValueError:
        print(Fore.RED + "⚠️ Debes escribir un número válido.")
    return None

# 🐣 Añadir criatura
def añadir_criatura(lista):
    print(Fore.LIGHTBLACK_EX + "(Puedes escribir 'cancelar' en cualquier campo para volver atrás)" + RESET)

    while True:
        nombre = limpiar_input(input("Nombre de la criatura: "), "capitalize")
        if nombre.lower() == "cancelar":
            print("🚪 Añadir criatura cancelado.")
            return
        if not es_input_valido(nombre):
            print(Fore.RED + "❌ Ese nombre no parece válido. Usa letras o números.")
        elif any(c["nombre"].lower() == nombre.lower() for c in lista):
            print(Fore.RED + f"❌ Ya existe una criatura llamada '{nombre}'. Usa otro nombre.")
        else:
            break

    while True:
        tipo = limpiar_input(input("Tipo de la criatura: "), "lower")
        if tipo.lower() == "cancelar":
            print("🚪 Añadir criatura cancelado.")
            return
        if tipo not in TIPOS_VALIDOS:
            print(Fore.RED + f"❌ Tipo no válido. Tipos permitidos: {', '.join(TIPOS_VALIDOS)}")
        else:
            break

    while True:
        nivel_input = input("Nivel de la criatura (1–100): ")
        nivel = validar_nivel(nivel_input)
        if nivel is not None:
            break

    etiquetas_input = input("Etiquetas (coma separadas, opcional): ").strip()
    if etiquetas_input.lower() == "cancelar":
        print("🚪 Añadir criatura cancelado.")
        return
    etiquetas = [limpiar_input(e, "lower") for e in etiquetas_input.split(",") if e.strip()] if etiquetas_input else []

    criatura = {
        "nombre": nombre,
        "tipo": tipo,
        "nivel": nivel,
        "etiquetas": etiquetas
    }

    lista.append(criatura)
    print(Fore.GREEN + f"✅ Criatura '{nombre}' añadida correctamente con {len(etiquetas)} etiqueta(s).")

# 🔍 Buscar criatura
def buscar_criatura(lista):
    if not lista:
        print(Fore.YELLOW + "🌫️ No hay criaturas registradas para buscar.")
        return

    termino = limpiar_input(input("🔎 Escribe el nombre o parte del nombre de la criatura: "), "lower")
    resultados = [c for c in lista if termino in c["nombre"].lower()]

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

# 🗑️ Eliminar criatura
def eliminar_criatura(lista):
    nombre = limpiar_input(input("Nombre de la criatura a eliminar: "), "lower")

    for criatura in lista:
        if criatura["nombre"].lower() == nombre:
            confirmacion = limpiar_input(input(Fore.RED + f"⚠️ ¿Estás seguro de que quieres eliminar '{criatura['nombre']}'? (s/n): " + RESET), "lower")
            if confirmacion == "s":
                lista.remove(criatura)
                print(Fore.GREEN + f"✅ Criatura '{criatura['nombre']}' eliminada con éxito." + RESET)
            else:
                print(Fore.LIGHTBLACK_EX + "❎ Operación cancelada." + RESET)
            return

    print(Fore.YELLOW + f"🧐 No se encontró ninguna criatura con el nombre '{nombre}'." + RESET)

# 📜 Mostrar todas las criaturas
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

# 📂 Mostrar por tipo
def mostrar_por_tipo(lista):
    if not lista:
        print(Fore.YELLOW + "🌫️ No hay criaturas registradas.")
        return

    tipos = set(c["tipo"] for c in lista)
    print(Fore.CYAN + "🔎 Tipos disponibles:")
    for tipo in tipos:
        print(f"- {tipo.capitalize()}")

    tipo_buscar = limpiar_input(input("¿Qué tipo quieres mostrar?: "), "lower")
    criaturas_filtradas = [c for c in lista if c["tipo"] == tipo_buscar]

    if criaturas_filtradas:
        print(Fore.MAGENTA + f"\n📜 Criaturas del tipo '{tipo_buscar.capitalize()}':")
        color_tipo = TIPO_COLORES.get(tipo_buscar, Fore.WHITE)
        for i, criatura in enumerate(criaturas_filtradas, 1):
            print(f"{color_tipo}{i}. {criatura['nombre'].capitalize()} (Nivel {criatura['nivel']}){RESET}")
    else:
        print(Fore.RED + "❌ No se encontraron criaturas de ese tipo.")

# 🛠️ Editar criatura
def editar_criatura(lista):
    if not lista:
        print(Fore.YELLOW + "🌫️ No hay criaturas para editar.")
        return

    mostrar_todas(lista)

    try:
        index = int(input("Número de la criatura que quieres editar: ").strip()) - 1
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
        criatura['nombre'] = limpiar_input(nuevo_nombre, "capitalize")

    nuevo_tipo = input(f"Nuevo tipo (Enter para mantener '{criatura['tipo']}'): ").strip()
    if nuevo_tipo:
        nuevo_tipo_limpio = limpiar_input(nuevo_tipo, "lower")
        if nuevo_tipo_limpio in TIPOS_VALIDOS:
            criatura['tipo'] = nuevo_tipo_limpio
        else:
            print(Fore.RED + f"⚠️ Tipo no válido. Se mantiene el actual: {criatura['tipo']}")
    nuevo_nivel = input(f"Nuevo nivel (1–100, Enter para mantener {criatura['nivel']}): ").strip()
    if nuevo_nivel:
        nivel_valido = validar_nivel(nuevo_nivel)
        if nivel_valido is not None:
            criatura['nivel'] = nivel_valido
        else:
            print(Fore.LIGHTBLACK_EX + "ℹ️ Se mantiene el nivel actual.")


    nuevas_etiquetas = input("Nuevas etiquetas (coma separadas, Enter para mantener las actuales): ").strip()
    if nuevas_etiquetas:
        criatura['etiquetas'] = [limpiar_input(e, "lower") for e in nuevas_etiquetas.split(",") if e.strip()]

    print(Fore.GREEN + "✅ Criatura editada correctamente.")

def cuenta_atras_dramatica():
    print(Fore.LIGHTBLACK_EX + "\nActivando modo dramático..." + Style.RESET_ALL)
    for i in range(5, 0, -1):
        print(Fore.LIGHTYELLOW_EX + f"⏳ {i}..." + Style.RESET_ALL)
        time.sleep(1)
    print(Fore.RED + "🔥 ¡Lanzamiento!" + Style.RESET_ALL)
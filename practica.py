
criaturas = []

def añadir_criatura(lista):
    try:
        nombre = input("Nombre de la criatura: ").strip().lower()
        if not nombre:
            raise ValueError("El nombre no puede estar vacío.")
        if any(c["nombre"] == nombre for c in lista):
            print("⚠️ Ya existe una criatura con ese nombre.")
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
        print(f"✅ Criatura '{nombre}' añadida con éxito.")
    except ValueError as ve:
        print(f"Error: {ve}")

def buscar_criatura(lista):
    nombre = input("🔎 Nombre de la criatura a buscar: ").strip().lower()
    for criatura in lista:
        if criatura["nombre"] == nombre:
            print("\n📌 Criatura encontrada:")
            print(f"- Nombre: {criatura['nombre'].capitalize()}")
            print(f"- Tipo: {criatura['tipo'].capitalize()}")
            print(f"- Nivel: {criatura['nivel']}")
            return
    print("❌ No se encontró ninguna criatura con ese nombre.")

def eliminar_criatura(lista):
    nombre = input("🗑️ Nombre de la criatura a eliminar: ").strip().lower()
    for criatura in lista:
        if criatura["nombre"] == nombre:
            print(f"⚠️ ¿Estás seguro de que quieres eliminar '{nombre}'?")
            confirmacion = input("Escribe 'sí' para confirmar: ").strip().lower()
            if confirmacion == "sí":
                lista.remove(criatura)
                print(f"✅ '{nombre}' ha sido eliminada.")
            else:
                print("❎ Eliminación cancelada.")
            return
    print("❌ No se encontró ninguna criatura con ese nombre.")

def mostrar_todas(lista):
    if not lista:
        print("🌫️ No hay criaturas registradas.")
    else:
        print("\n📜 Tu colección de criaturas:")
        for i, criatura in enumerate(lista, 1):
            print(f"{i}. {criatura['nombre'].capitalize():20} | Tipo: {criatura['tipo'].capitalize():10} | Nivel: {criatura['nivel']}")

def cargar_desde_archivo(lista, archivo="criaturas.txt"):
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            for linea in f:
                partes = linea.strip().split(",")
                if len(partes) != 3:
                    continue
                nombre, tipo, nivel = partes
                if not nivel.isdigit():
                    continue
                criatura = {
                    "nombre": nombre.strip().lower(),
                    "tipo": tipo.strip().lower(),
                    "nivel": int(nivel)
                }
                if not any(c["nombre"] == criatura["nombre"] for c in lista):
                    lista.append(criatura)
        print("✅ Datos cargados correctamente.")
    except FileNotFoundError:
        print("⚠️ Archivo no encontrado. Aún no hay datos guardados.")

def guardar_en_archivo(lista, archivo="criaturas.txt"):
    try:
        with open(archivo, "w", encoding="utf-8") as f:
            for criatura in lista:
                linea = f"{criatura['nombre']},{criatura['tipo']},{criatura['nivel']}\n"
                f.write(linea)
        print("💾 Datos guardados correctamente.")
    except Exception as e:
        print(f"❌ Error al guardar: {e}")

def mostrar_menu():
    print("\n🌟 Menú de opciones:")
    print("1. Añadir criatura")
    print("2. Buscar criatura")
    print("3. Eliminar criatura")
    print("4. Mostrar todas")
    print("5. Cargar desde archivo")
    print("6. Guardar en archivo")
    print("7. Salir")

cargar_desde_archivo(criaturas)

while True:
    mostrar_menu()
    opcion = input("Elige una opción (1-7): ").strip()

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
        print("📂 Cargar desde archivo")
        cargar_desde_archivo(criaturas)
    elif opcion == "6":
        print("💾 Guardar en archivo")
        guardar_en_archivo(criaturas)
    elif opcion == "7":
        guardar_en_archivo(criaturas)
        print("👋 Datos guardados. Saliendo del programa. ¡Hasta la próxima!")
        break

    else:
        print("⚠️ Opción no válida.")

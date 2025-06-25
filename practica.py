# Flor de Silicio · Sesión 4 – Gestión de Criaturas Mágicas 🐉✨

def mostrar_menu():
    print("\n🌟 Menú de opciones:")
    print("1. Añadir criatura")
    print("2. Borrar criatura")
    print("3. Buscar criatura")
    print("4. Mostrar todas las criaturas")
    print("5. Salir")

def mostrar_criaturas(lista):
    if not lista:
        print("🌫️ No hay criaturas registradas todavía.")
    else:
        print("\n📜 Tu colección de criaturas:")
        for i, criatura in enumerate(sorted(lista), 1):
            print(f"{i}. {criatura.capitalize()}")

def buscar_criatura(lista, nombre):
    return nombre in lista
    
# Lista donde guardaremos las criaturas
criaturas = []

# Inicio del programa
print("🌱 Bienvenido/a al Gestor de Criaturas Mágicas 🧙‍♂️")
print("Usa el menú para interactuar con tu colección.\n")

while True:
    mostrar_menu()
    opcion = input("Elige una opción (1-5): ")

    if opcion == "1":
        print("👉 Opción: Añadir criatura")
        try:
            nueva = input("Introduce el nombre de la criatura: ").strip().lower()
            if not nueva:
                raise ValueError("El nombre no puede estar vacío.")
            if nueva in criaturas:
                print("⚠️ Esa criatura ya está en tu lista.")
            else:
                criaturas.append(nueva)
                print(f"✅ {nueva.capitalize()} añadida correctamente.")
        except ValueError as ve:
            print(f"Error: {ve}")

    elif opcion == "2":
        print("👉 Opción: Borrar criatura")
        # aquí pondremos el código para borrar
    elif opcion == "3":
        nombre = input("🔍 Nombre de la criatura a buscar: ").strip().lower()
        if buscar_criatura(criaturas, nombre):
            print(f"✅ {nombre.capitalize()} está en tu colección.")
        else:
            print(f"❌ {nombre.capitalize()} no está en la lista.")

    elif opcion == "4":
        mostrar_criaturas(criaturas)

    elif opcion == "5":
        print("👋 Saliendo del programa. ¡Hasta la próxima!")
        break
    else:
        print("⚠️ Opción no válida. Por favor, introduce un número del 1 al 5.")

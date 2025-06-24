# 🌱 Mini App PRO: Catálogo de Colores

# 1) Estructura base
catalogo = [
    ["Rojo", "Azul"],
    ["Verde", "Amarillo"]
]

print("📋 Catálogo actual:")
for i, g in enumerate(catalogo):
    print(f"Grupo {i}: {g}")
    for c in g:
        print(f"  • {c}")

print("\n✨ Vamos a añadir colores. Escribe 'salir' cuando termines.\n")

# 2) Bucle principal
while True:
    grupo_input = input("¿A qué grupo quieres añadir colores? (0 o 1): ")
    if grupo_input.lower() == "salir":
        break

    # Validar grupo
    if not grupo_input.isdigit() or int(grupo_input) not in [0, 1]:
        print("⚠️ Grupo no válido. Elige 0 o 1.")
        continue

    grupo = int(grupo_input)

    modo = input("¿Quieres añadir un color o varios? (uno/varios): ").lower()

    if modo == "salir":
        break

    if modo == "uno":
        color = input("Escribe el color: ").strip().capitalize()
        catalogo[grupo].append(color)

    elif modo == "varios":
        colores = input("Escribe los colores separados por coma: ")
        lista_colores = [c.strip().capitalize() for c in colores.split(",")]
        catalogo[grupo].extend(lista_colores)

    else:
        print("⚠️ Modo no válido. Usa 'uno' o 'varios'.")
        continue

    print("\n✅ Catálogo actualizado:")
    for i, g in enumerate(catalogo):
        print(f"Grupo {i}: {g}")
        for c in g:
            print(f"  • {c}")

    print("\n✨ Puedes seguir añadiendo o escribir 'salir' para terminar.\n")

print("\n🚀 Catálogo final:")
for i, g in enumerate(catalogo):
    print(f"Grupo {i}: {g}")
    for c in g:
        print(f"  • {c}")

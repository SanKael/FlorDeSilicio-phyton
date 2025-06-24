
catalogo = [
    ["rojo", "azul"],
    ["verde", "amarillo"]
]

grupo = int(input("¿A qué grupo quieres añadir colores? (0 o 1): "))
modo = input("¿Quieres añadir un color o varios? (uno/varios): ")

if modo == "uno":
    color = input("Escribe el color: ")
    catalogo[grupo].append(color)

elif modo == "varios":
    colores = input("Escribe los colores separados por coma: ")
    lista_colores = colores.split(",")
    # Limpiar espacios en blanco de cada color
    lista_colores = [color.strip() for color in lista_colores]
    catalogo[grupo].extend(lista_colores)

else:
    print("Modo no válido. Usa 'uno' o 'varios'.")

print("\n📋 Catálogo actualizado:")
for i, g in enumerate(catalogo):
    print(f"Grupo {i}: {g}")
    for c in g:
        print(f"  • {c}")

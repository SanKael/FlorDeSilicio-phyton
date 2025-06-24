catalogo = [
    ["rojo", "azul"],
    ["verde", "amarillo"]
]

grupo = int(input("¿A qué grupo quieres añadir colores? (0 o 1): "))

if modo == "uno":
  color = input("Escribe el color: ")
  catalogo[grupo].append(color)

elif modo == "varios":
colores = input("Escribe los colores separados por coma: ")
lista_colores = colores.split(",")
catalogo[grupo].extend(lista_colores)

for g in catalogo:
  print("Grupo:", g)
  for c in g:
      print("  Color:", c)

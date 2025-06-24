# 🌱 Flor de Silicio — Resumen TODO EN UNO

# 1️⃣ Variables y print
nombre = input("¿Cómo te llamas? ")
print(f"Hola, {nombre.capitalize()} 🌱")

# 2️⃣ Condicional simple
edad = int(input("¿Cuántos años tienes? "))
if edad < 18:
    print("Eres menor de edad.")
elif edad == 18:
    print("Tienes justo 18, mayor recién estrenado.")
else:
    print("Eres mayor de edad.")

# 3️⃣ Bucle for con range
print("\nNúmeros del 1 al 5:")
for i in range(1, 6):
    print(i)

# 4️⃣ Bucle while
print("\nAdivina el número secreto (entre 1 y 5)")
secreto = 3
numero = 0
while numero != secreto:
    numero = int(input("Tu número: "))
    if numero == secreto:
        print("¡Correcto!")
    else:
        print("Prueba otra vez.")

# 5️⃣ Lista y operaciones básicas
colores = ["Rojo", "Azul"]
print(f"\nColores iniciales: {colores}")

# Append
colores.append("Verde")
print(f"Después de append: {colores}")

# Remove
colores.remove("Azul")
print(f"Después de remove: {colores}")

# Index
pos = colores.index("Verde")
print(f"Posición de Verde: {pos}")

# 6️⃣ Lista dentro de lista y recorrido anidado
catalogo = [
    ["Rojo", "Amarillo"],
    ["Verde", "Morado"]
]

print("\n🎨 Catálogo completo:")
for i, grupo in enumerate(catalogo):
    print(f"Grupo {i}: {grupo}")
    for color in grupo:
        print(f"  • {color}")

# 7️⃣ Función simple con return
def saludar(persona):
    return f"¡Un saludo para ti, {persona}!"

print("\n" + saludar(nombre.capitalize()))

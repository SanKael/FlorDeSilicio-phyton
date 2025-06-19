print("¡Hola! Vamos a jugar con los animales.")

# Lista de animales aceptados
animales = ["perro", "gato", "pez"]

# Input del usuario
favorito = input("¿Cuál es tu animal favorito?\n")

# Variable bandera para saber si encontramos coincidencia
encontrado = False

# Bucle para recorrer la lista
for animal in animales:
    if favorito.lower() == animal:
        if animal == "perro":
            print("¡Guau! Los perros son geniales.")
        elif animal == "gato":
            print("¡Miau! Los gatos son muy divertidos.")
        elif animal == "pez":
            print("¡Glub! Los peces son muy interesantes.")
        encontrado = True

# Si no está en la lista
if not encontrado:
    print(f"¡{favorito.capitalize()}! Es un animal muy especial.")

print("Gracias por jugar conmigo. ¡Adiós!")
def responder(favorito):
    # Diccionario de animales y respuestas
    respuestas = {
        "perro": "¡Guau! Los perros son geniales.",
        "gato": "¡Miau! Los gatos son muy divertidos.",
        "pez": "¡Glub! Los peces son muy interesantes.",
        "loro": "¡Hola! ¡Soy un loro parlanchín! 🦜",
        "conejo": "¡Saltitos! Los conejos son adorables. 🐰",
        "tortuga": "¡Vamos! Las tortugas son muy lentas. 🐢",
        "elefante": "¡Trompa! Los elefantes son muy grandes. 🐘",
        "jirafa": "¡Altas! Las jirafas son muy altas. 🦒",
        "león": "¡Rugido! Los leones son muy fuertes. 🦁",
        "tigre": "¡Rugido! Los tigres son muy fuertes. 🐅",
        "oso": "¡Gruñido! Los osos son muy fuertes. 🐻"
    }

    # Buscar el animal en el diccionario
    if favorito.lower() in respuestas:
        print(respuestas[favorito.lower()])
    else:
        print(f"¡{favorito.capitalize()}! Es un animal muy especial.")

def despedir():
    print("Gracias por jugar conmigo. ¡Adiós! 🌸")

# 🌱 Bucle principal usando WHILE:
while True:
    # Pide al usuario un animal
    favorito = input("Dime un animal o escribe 'salir' para terminar:\n")

    # Si escribe 'salir', rompe el bucle
    if favorito.lower() == "salir":
        break

    # Llama a la función responder para dar la respuesta del animal
    responder(favorito)

# Cuando sale del bucle, llama a la despedida
despedir()

def saludar():
    print("¡Hola! Vamos a jugar con los animales.")
    favorito = input("¿Cuál es tu animal favorito?\n")
    return favorito

def responder(favorito):
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

    if favorito.lower() in respuestas:
        print(respuestas[favorito.lower()])
    else:
        print(f"¡{favorito.capitalize()}! Es un animal muy especial.")

def despedir():
    print("Gracias por jugar conmigo. ¡Adiós!")

# Llamadas a las funciones
favorito = saludar()
responder(favorito)
despedir()
print("¡Hola! Vamos a jugar con los animales.")

# Diccionario: clave = animal, valor = respuesta única
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

# Input del usuario
favorito = input("¿Cuál es tu animal favorito?\n")

# Buscar si el animal está en el diccionario
if favorito.lower() in respuestas:
    print(respuestas[favorito.lower()])
else:
    print(f"¡{favorito.capitalize()}! Es un animal muy especial.")

print("Gracias por jugar conmigo. ¡Adiós!")

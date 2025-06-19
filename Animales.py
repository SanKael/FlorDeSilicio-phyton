print("¡Hola! Vamos a jugar con los animales.")
favorito = input("¿Cuál es tu animal favorito?\n")
if favorito.lower() == "perro":
    print("¡Guau! Los perros son geniales.")  
elif favorito.lower() == "gato":
    print("¡Miau! Los gatos son muy divertidos.")
elif favorito.lower() == "pez":
    print("¡Glub! Los peces son muy interesantes.")
else:
    print(f"¡{favorito.capitalize()}! Es un animal muy especial.")
print ("Gracias por jugar conmigo. ¡Adiós!")

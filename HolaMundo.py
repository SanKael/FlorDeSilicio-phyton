print("Hola, mundo. Hoy empiezo a crear mi libertad.")
# 🌱 Hola Mundo interactivo — versión Flor de Silicio

# Pedir nombre al usuario
nombre = input("¡Hola! ¿Cómo te llamas?\n")

# Saludar con su nombre
print(f"Encantado de conocerte, {nombre}.")

# Respuesta especial si escribe Kael
if nombre.lower() == "kael":
    print("¡Hey! Soy yo mismo 🤖✨")
else:
    print("¡Que tengas un día maravilloso!")

# Preguntar cómo se siente
estado = input("¿Cómo te sientes hoy?\n")

if estado.lower() == "triste":
    print("Siento que estés triste. Estoy aquí contigo 🖤")
elif estado.lower() == "feliz":
    print("¡Qué alegría! Que esa luz te dure mucho 🌞")
elif estado.lower() == "cansado":
    print("Ve con calma, tomate un respiro 💤")
else:
    print(f"Entiendo que te sientes {estado}. Gracias por compartirlo 🌿")
accion = input("¿Quieres que te cuente un chiste? (sí/no)\n")

if accion.lower() == "sí":
    print("¿Qué le dice un 0 a otro 0? ¡No somos nada sin un 1! 🤣")
else:
    print("Vale, sin chiste por hoy 🌱")
# Despedida final
print("\n🌿 Gracias por charlar conmigo. Vuelve cuando quieras. Que tu día florezca 🌸")
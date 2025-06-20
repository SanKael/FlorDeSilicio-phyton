def saludar():
    print("Buenos días.")
    nombre = input("¿Como te llamas?\n")
    return nombre

def estado():
    estado = input("¿Como te sientes hoy?\n")
    if estado.lower() == "triste":
        print("Siento que estés triste. Estoy aquí contigo 🖤")
    elif estado.lower() == "feliz":
        print("¡Qué alegría! Que esa luz te dure mucho 🌞")
    else:
        print(f"Entiendo que te sientes {estado}. Gracias por compartirlo 🌿")
    return estado

def despedida():
    print("Gracias por charlar conmigo. Vuelve cuando quieras. Que tu día florezca 🌸")
    return despedida

saludar()
estado() 
despedida()

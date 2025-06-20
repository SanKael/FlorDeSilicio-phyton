def saludar():
  print("Buenos días.")
  nombre = input("¿Cómo te llamas?\n")
  return nombre

def estado(nombre):
  estado = input(f"¿Cómo te sientes hoy, {nombre}?\n")
  if estado.lower() == "triste":
      print("Siento que estés triste. Estoy aquí contigo 🖤")
  elif estado.lower() == "feliz":
      print("¡Qué alegría! Que esa luz te dure mucho 🌞")
  else:
      print(f"Entiendo que te sientes {estado}. Gracias por compartirlo 🌿")

def despedida():
  print("Gracias por charlar conmigo. Vuelve cuando quieras. Que tu día florezca 🌸")

# Llamadas
nombre = saludar()
estado(nombre)
despedida()

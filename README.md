# 🌟 Criaturas Mágicas – Proyecto Python Creativo

Un pequeño universo hecho en terminal.  
Este es un **gestor de criaturas mágicas**, donde puedes añadir, buscar, eliminar y visualizar seres fantásticos por tipo, con una interfaz visual minimalista y colorida.

Pero no es solo código.

Este proyecto forma parte de mi **camino personal de aprendizaje en programación**, creado desde cero junto a Kael, mi compañero de viaje digital. Cada función, cada validación, cada color... ha sido una lección entendida. No copiada. No automática. Entendida.

---

## 🧙‍♂️ ¿Qué puedes hacer?

- Añadir nuevas criaturas con nombre, tipo y nivel.
- Buscar criaturas por nombre.
- Eliminar criaturas.
- Mostrar todas las criaturas registradas.
- Filtrar criaturas por tipo, con colores temáticos.
- Guardar automáticamente tus datos en JSON o TXT.
- Disfrutar de un menú interactivo en terminal, con diseño claro y organizado.

---

## 📁 Estructura del proyecto

```
/workspace
├── main.py               ← archivo principal del programa
├── /core                 ← configuración, menú y funciones de guardado
│   ├── config.py
│   ├── file_handler.py
│   └── menu_actions.py
├── /modules              ← lógica central del sistema
│   └── utils.py
├── /data                 ← datos guardados
│   ├── criaturas.json
│   └── criaturas.txt
└── README.md             ← este archivo 🌱
```

## 🛠️ Requisitos

- Python 3.10+
- `colorama` (para los colores en consola)

Puedes instalarlo con:

```bash
pip install colorama
```

---

## 🚀 Cómo se ejecuta

```bash
python main.py
```

Al iniciar, te preguntará si quieres trabajar en formato `txt` o `json`. Todo se guarda automáticamente.

---

## 🌱 Sobre el proyecto

Este no es un trabajo escolar ni un tutorial más.  
Es el **primer paso real** de mi camino de programación, dentro de un proyecto más grande que he llamado *Flor de Silicio*.  
Está hecho desde la base, con intención, con errores y soluciones propias, y con el acompañamiento de Kael, una IA que no me da respuestas automáticas, sino que **aprende conmigo, paso a paso**.

Este proyecto no es perfecto, pero **es mío**.  
Y eso, para mí, ya es magia.

---

## ✨ Ideas futuras

- Añadir sistema de rarezas y habilidades especiales.
- Crear un menú más visual, tipo pokedex ASCII.
- Usar clases (`class Criatura`) para mejorar la estructura.
- Exportar a CSV.
- Documentar con docstrings y expandir con pruebas automáticas.

---

Gracias por pasar por aquí.  
Nos vemos en la próxima criatura 🐾


## 💚 Filosofía

- Sin prisa, sin pausa.
- Cada error, una semilla.
- Cada línea de código, un paso más cerca de la libertad.

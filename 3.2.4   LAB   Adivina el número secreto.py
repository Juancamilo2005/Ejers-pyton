secret_number = 777

print("""
+================================+
| ¡Bienvenido a mi juego, muggle!|
| Introduce un número entero     |
| y adivina qué número he        |
| elegido para ti.               |
+================================+
""")

while True:
    guess = int(input("¿Cuál es el número secreto? "))
    if guess == secret_number:
        print("¡Felicidades! Has adivinado el número secreto.")
        break
    else:
        print("Ese no es el número secreto. Inténtalo de nuevo.")

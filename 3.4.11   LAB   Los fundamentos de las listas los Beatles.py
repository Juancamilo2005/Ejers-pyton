# Paso 1: Crear una lista vacía llamada beatles
beatles = []

print("Paso 1:", beatles)

# Paso 2: Agregar los miembros originales de la banda
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")

print("Paso 2:", beatles)

# Paso 3: Pedir al usuario que agregue nuevos miembros usando un bucle for y append()
new_members = ["Stu Sutcliffe", "Pete Best"]
for member in new_members:
    beatles.append(member)

print("Paso 3:", beatles)

# Paso 4: Eliminar a Stu Sutcliffe y Pete Best de la lista
del beatles[3:5]  # Eliminamos los elementos en las posiciones 3 y 4 (Stu Sutcliffe y Pete Best)

print("Paso 4:", beatles)

# Paso 5: Agregar a Ringo Starr al principio de la lista usando insert()
beatles.insert(0, "Ringo Starr")

print("Paso 5:", beatles)

# Imprimir la longitud final de la lista
print("Número de los integrantes de la banda", beatles

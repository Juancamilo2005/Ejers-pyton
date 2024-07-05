hat_list = [1, 2, 3, 4, 5]  # Esta es una lista existente de números ocultos en el sombrero.

# Paso 1: Solicitar al usuario reemplazar el número del medio con un número entero ingresado por el usuario.
user_number = int(input("Ingrese un número entero para reemplazar el número del medio: "))
hat_list[len(hat_list) // 2] = user_number  # Reemplazamos el número del medio

# Paso 2: Eliminar el último elemento de la lista.
hat_list.pop()

# Paso 3: Imprimir la longitud de la lista existente.
print("La longitud de la lista es:", len(hat_list))

print(hat_list)

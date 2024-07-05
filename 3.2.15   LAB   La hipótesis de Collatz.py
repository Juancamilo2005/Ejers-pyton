c0 = int(input("Ingrese un número natural (entero positivo): "))
steps = 0

while c0 != 1:
    print(c0, end=' ')
    if c0 % 2 == 0:
        c0 = c0 // 2
    else:
        c0 = 3 * c0 + 1
    steps += 1

print(c0)  
print(f"Se necesitaron {steps} pasos para alcanzar 1.")

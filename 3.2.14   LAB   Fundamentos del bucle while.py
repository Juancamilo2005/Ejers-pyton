blocks = int(input("Ingresa el número de bloques: "))


height = 0
blocks_used = 0

while True:
    height += 1
    blocks_used += height
    if blocks_used > blocks:
        height -= 1
        break


	

print("La altura de la pirámide:", height)


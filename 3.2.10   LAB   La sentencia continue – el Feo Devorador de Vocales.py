user_word = input("Por favor, ingresa una palabra: ")
user_word = user_word.upper()  

for letter in user_word:
    if letter == 'A' or letter == 'E' or letter == 'I' or letter == 'O' or letter == 'U':
        continue  
    print(letter)  

# Користувачем вводиться два імені. Використовуючи конструкцію 
# розгалуження програма повинна вивести імена в алфавітному порядку.

# Вхідні дані:

# Guido van Rossum
# Dennis Ritchie
# Вихідні дані:

# Dennis Ritchie
# Guido van Rossum

#*============Code================

# Зчитуємо два імені від користувача
name1 = input("Введіть перше ім'я: ")
name2 = input("Введіть друге ім'я: ")

# Виводимо імена в алфавітному порядку
if name1 < name2:
    print(name1)
    print(name2)
else:
    print(name2)
    print(name1)
# Надрукувати у рядку m разів число n. Числа m і n - цілі числа, які вводить користувач у порядку n, m.

# Вхідні дані:

# 10
# 5
# Вихідні дані:

# 10 10 10 10 10

#*============Code================

n = int(input("Введіть ціле число: "))
m = int(input("Введіть ціле число, яке вкаже на кількість повторувань при відображенні на екрані: "))

# Зчитуємо два цілі числа n і m з клавіатури

# Виводимо число n у рядку m разів
result = (str(n) + ' ') * m
print(result.strip())

# метод strip() використовується для видалення пробілів та символів нового рядка з обох кінців рядка. 
# Це дозволяє очистити рядок від зайвих пробілів та символів нового рядка, що може бути корисним при 
# обробці введених даних або при роботі з рядками.

# Метод strip() не тільки видаляє пробіли, але й будь-які інші символи з країв рядка. 
# Якщо потрібно видалити тільки пробіли, можна використовувати метод rstrip() для видалення пробілів справа 
# або lstrip() для видалення пробілів зліва.
# Напишіть програму, яка приймає ціле число n і обчислює значення виразу n + nn + nnn.

# Вхідні дані:

# 5
# 3
# 1
# Вихідні дані:

# 615
# 369
# 123

#*============Code================

# Зчитуємо ціле число n з клавіатури
print("Введіть ціле число")
n = int(input())

# Обчислюємо значення виразу n + nn + nnn
result = n + int(str(n) * 2) + int(str(n) * 3)
# Другій варіант
# result = n*1 + n*11 + n*111
# Виводимо результат
print("\nОбчислення значення виразу n + nn + nnn для числа", n, "дорівнює", result)
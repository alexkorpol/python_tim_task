# Напишіть програму для виведення усіх цілих чисел від 20 до n включно (n > 20), 
# де n - ціле число, яке вводить користувач.

# Вхідні дані:

# 25
# Вихідні дані:

# 20
# 21
# 22
# 23
# 24
# 25

#*============Code================

# Зчитуємо ціле число n з клавіатури
n = int(input("Введіть ціле число n (n > 20): "))

# Перевіряємо, чи введене число відповідає умові n > 20
if n > 20:
    # Виводимо усі цілі числа від 20 до n включно
    for i in range(20, n + 1):
        print(i)
else:
    print("Введене число не задовольняє умові n > 20.")
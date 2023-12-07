# Дано маси і об’єми двох тіл, виготовлених з різних матеріалів (дійсні числа). 
# Матеріал якого з тіл має більшу густину? Введення величин відбувається
# у такому порядку: m1, v1, m2, v2.

# Вхідні дані:

# 2
# 3.5
# 1.5
# 2.3
# Вихідні дані:

# 1.5 2.3

#*============Code================

# Зчитуємо маси і об'єми з клавіатури
m1 = float(input("Введіть масу тіла 1: "))
v1 = float(input("Введіть об'єм тіла 1: "))
m2 = float(input("Введіть масу тіла 2: "))
v2 = float(input("Введіть об'єм тіла 2: "))

# Обчислюємо густини тіл
density1 = m1 / v1
density2 = m2 / v2

# Порівнюємо густини та виводимо результат
if density1 > density2:
    print(f"{m2} {v2}")
else:
    print(f"{m1} {v1}")
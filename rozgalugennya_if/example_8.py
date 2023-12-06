# Дано радіус кола і сторона квадрата (дійсні числа). У якої фігури площа більше?

# Вхідні дані:

# 2.5
# 3.5
# 3.6
# 7.5
# Вихідні дані:

# Circle
# Square

#*============Code================

import math

# Зчитуємо радіус та сторону з клавіатури
radius = float(input("Введіть радіус кола: "))
side = float(input("Введіть сторону квадрата: "))

# Обчислюємо площі фігур
area_circle = math.pi * radius ** 2
area_square = side ** 2

# Порівнюємо площі та виводимо результат
if area_circle > area_square:
    print("Circle")
else:
    print("Square")
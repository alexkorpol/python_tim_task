# Напишіть програму для друку чисел, у яких розділювачами груп розрядів (групи по три цифри) є коми.

# Вхідні дані:

# 10000000
# 1000
# 12003
# Вихідні дані:

# 10,000,000
# 1,000
# 12,003
 
# *================= Code =====================
# Зчитуємо числа з клавіатури
number1 = int(input())
number2 = int(input())
number3 = int(input())

# Виводимо числа з комами як розділювачами груп розрядів
print("{:,}".format(number1))
print("{:,}".format(number2))
print("{:,}".format(number3))
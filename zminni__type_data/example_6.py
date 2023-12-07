# Напишіть програму, яка отримує три цілих числа, введені з клавіатури 
# (кожне число вводиться на окремому рядку), і друкує на екрані їх суму, 
# добуток, результат піднесення першого числа до степеня різниці другого і третього чисел.

# Вхідні дані:

# 2
# 3
# 6
# Вихідні дані:

# 11
# 36
# 0.125
#*============Code================

# Зчитуємо три цілих числа з клавіатури
num1 = int(input("Введіть перше ціле число "))
num2 = int(input("Введіть друге ціле число "))
num3 = int(input("Введіть третє ціле число "))

# Обчислюємо суму, добуток та результат піднесення до ступеня
sum_result = num1 + num2 + num3
product_result = num1 * num2 * num3
power_result = num1 ** (num2 - num3)

# Виводимо результати
print("\t*************************")
print("\t* Результати обчислення *")
print("\t*************************")
print("Сума трьох чисел", sum_result)
print("Добуток трьох чисел", product_result)
print(f"Результат піднесення першого числа {num1} до степеня різниці другого {num2} і третього чисел {num3} => {power_result}")
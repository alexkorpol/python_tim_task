# Напишіть програму, щоб вивести символ за введеним ASCII значенням.

# Вхідні дані:

# 97
# 121
# 55
# Вихідні дані:

# a
# y
# 7

#*============Code================

# Зчитуємо ASCII значення з клавіатури
ascii_value_1 = int(input("Введіть код ASCII першого символу "))
ascii_value_2 = int(input("Введіть код ASCII другого символу "))
ascii_value_3 = int(input("Введіть код ASCII третього символу "))

# Отримуємо символи для введених ASCII значень
char_1 = chr(ascii_value_1)
char_2 = chr(ascii_value_2)
char_3 = chr(ascii_value_3)

# Виводимо символи
# print("\nПерший символ")
print("\nПерший символ", char_1)
# print("\tДругий символ")
print( "\tДругий символ", char_2)
# print("\t\tТретій символ")
print("\t\tТретій символ", char_3)
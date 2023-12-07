# Напишіть програму, щоб отримати ASCII значення введеного з клавіатури символа.

# Вхідні дані:

# G
# w
# +
# Вихідні дані:

# 71
# 119
# 43
#*============Code================
# Зчитуємо символи з клавіатури
input_char_1 = input("Введить перший символ з клавіатури ")
input_char_2 = input("Введить другий символ з клавіатури ")
input_char_3 = input("Введить третій символ з клавіатури ")

# Отримуємо ASCII значення для введених символів
ascii_value_1 = ord(input_char_1)
ascii_value_2 = ord(input_char_2)
ascii_value_3 = ord(input_char_3)

# Виводимо ASCII значення
print("Код ASCII першого символу", ascii_value_1)
print("Код ASCII другого символу", ascii_value_2)
print("Код ASCII третього символу", ascii_value_3)
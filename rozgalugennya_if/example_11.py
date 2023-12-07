# Напишіть програму, яка друкує Yes, якщо вводяться рядки yes або YES або Yes, у інших випадках друкує No.

# Вхідні дані:

# yes
# YES
# definitely
# Вихідні дані:

# Yes
# Yes
# No


#*============Code================

# Зчитуємо 
input_str1 = input(">>>")

# Перевіряємо умову і виводимо Yes або No
if input_str1.lower() == "yes" or input_str1.upper() == "YES":
    print("Yes")
else:
    print("No")


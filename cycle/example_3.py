# Напишіть програму-таймер зворотного відліку, яка запитує у користувача 
# кількість секунд n, з якої слід починати відлік.

# Вхідні дані:

# 5
# Вихідні дані:

# 5
# 4
# 3
# 2
# 1
# Start!

#*============Code================

# Зчитуємо кількість секунд n з клавіатури
n = int(input("Введіть кількість секунд: "))

# Виводимо зворотний відлік
for i in range(n, 0, -1):
    print(i)
    
# Виводимо повідомлення "Start!"
print("Start!")
# Напишіть програму, в якій користувач вводить пароль і якщо він співпадає із наперед 
# визначеним паролем для цього користувача, то виводиться повідомлення Password accepted.
# У іншому випадку повідомлення буде Sorry, that is the wrong password..

# Вхідні дані:

# starlink
# 12345
# Вихідні дані:

# Password accepted.
# Sorry, that is the wrong password.

#*============Code================


# Задаємо наперед визначений пароль для користувача
correct_password = "starlink"

# Зчитуємо пароль від користувача
user_password = input("Введіть пароль: ")

# Перевіряємо, чи введений пароль співпадає з наперед визначеним
if user_password == correct_password:
    print("Password accepted.")
else:
    print("Sorry, that is the wrong password.")
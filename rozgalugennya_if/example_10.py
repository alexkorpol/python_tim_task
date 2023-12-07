# Серед учнів школи проводилося тестування з трьох предметів, 
# по кожному з яких учні отримали певну кількість балів (цілі числа). 
# Напишіть програму, яку можуть використати учні для обчислення їхнього 
# середнього балу трьох тестів і виведення середнього значення. 
# Окрім того, необхідно передбачити виведення повідомлення 
# Congratulations! That is a great average!, якщо середній бал більший ніж 95.

# Вхідні дані:

# 143
# 112
# 135
# Вихідні дані:

# 130.00
# Congratulations! That is a great average!

#*============Code================

subject_1 = int(input("Введіть кількість балів за перший предмет: "))
subject_2 = int(input("Введіть кількість балів за другий предмет: "))
subject_3 = int(input("Введіть кількість балів за третій предмет: "))

average = (subject_1+subject_2+subject_3)/3
print(f"Середній бал: ", end=' ')
print("{:.2f}".format(average))
if average > 95:
    print("Congratulations! That is a great average!")
    
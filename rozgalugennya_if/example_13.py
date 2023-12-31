# В університеті використовується наступна шкала для інтерпретації 
# результатів тестування студентів: 90 балів і вище (A), 80-89 (B), 70-79 (C), 60-69 (D), нижче 60 (F). 
# Напишіть програму, яка дозволить студенту ввести тестовий бал, а потім відобразити оцінку для цього балу.

# Вхідні дані:

# 95
# 48
# 74
# Вихідні дані:

# Your grade is A.
# Your grade is F.
# Your grade is C.

#*============Code================
# Зчитуємо тестовий бал студента з клавіатури
test_score = float(input("Введіть тестовий бал (90-50): "))

# Визначаємо оцінку за шкалою
if test_score >= 90:
    grade = "A"
elif 80 <= test_score < 90:
    grade = "B"
elif 70 <= test_score < 80:
    grade = "C"
elif 60 <= test_score < 70:
    grade = "D"
else:
    grade = "F"

# Виводимо результат
print(f"Your grade is {grade}.")
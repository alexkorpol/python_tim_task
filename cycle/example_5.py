# Заполнение массива с клавиатуры элементами, которые все расположены в одной строке немного сложнее.
# Необходимо считать строку, разбить ее на элементы, а затем каждый элемент преобразовать в целое число

s = input("Введіть послідовність чисел через пробіл: ").split() 
print("s = ", s)
A = [int(i) for i in s] 
print(">>>>", A)
for i in range(len(A)):
    # other variant
    print(A[i], end=" ")
print()

#  Второй вариант
B = list(map(int, input("Введіть послідовність чисел через пробіл (варіант 2): ").split())) # встроенная функция list() преобразует последовательность в изменяемый список
                                    
print(">>>> B", B)
print(">>>>>> *B", *B)   # выводит массив без квадратных скобок
# Вводиться ціле невід’ємне число n (n ≤ 100). Виведіть піднесення числа 2 до степеня n.

# Вхідні дані:

# 10
# 12
# 5
# Вихідні дані:

# 1024
# 4096
# 32

# *================= Code =====================

n = int(input("\nВведіть ціле невід’ємне число n ≤ 100"))
power_n = 2 ** n
print(f"\nПіднесення числа 2 до степеня  {n} становить {power_n}. ")
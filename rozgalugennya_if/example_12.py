# Напишіть програму, яка визначає поведінку космічного апарата, що стартує на екваторі, 
# залежно від його початкової швидкості v, заданої у км/с (дійсні числа).
# Як ви знаєте з уроків фізики, тут можливі чотири випадки: 
# при v < 7,8 км/с апарат впаде на поверхню Землі; 
# при 7,8 ≤ v < 11,2 км/с апарат стане супутником Землі; 
# при 11,2 ≤ v < 16,4 км/с апарат стане супутником Сонця; 
# при v ≥ 16,4 км/с космічний апарат покине Сонячну систему.

# Вхідні дані:

# 12.5
# 22.56
# 8.3
# Вихідні дані:

# The device became a satellite of the Sun.
# The device left the Solar system.
# The device became a satellite of the Earth.

#*============Code================

# Зчитуємо початкову швидкість космічного апарата з клавіатури
velocity = float(input("Введіть початкову швидкість (км/с): "))

# Визначаємо поведінку апарата
if velocity < 7.8:
    print("The device will fall onto the Earth's surface.")
elif 7.8 <= velocity < 11.2:
    print("The device became a satellite of the Earth.")
elif 11.2 <= velocity < 16.4:
    print("The device became a satellite of the Sun.")
else:
    print("The device left the Solar system.")
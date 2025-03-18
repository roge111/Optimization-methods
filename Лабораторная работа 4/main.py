from MethodCoordinate import coordinate_descent
from MethodGradient import gradient_descent
from SpeedMethod import steepest_descent

import numpy as np


print("Метод покоординатного спуска")
print(coordinate_descent(2, 3, 500, 0.005))

print("Метод градиентного спуска")

# Начальные значения переменных
x0 = np.array([2, 3])  # Например, начальная точка (x1, x2) = (2, 3)

# Запуск градиентного спуска
alpha = 0.01  # Шаг обучения
result, f_min = gradient_descent(x0, alpha)

print(print(f"Минимум функции достигается при x = {result}, значение f = {f_min}"))


print("Метод наискорейшего спуска")



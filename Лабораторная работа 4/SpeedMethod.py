import numpy as np
from scipy.optimize import minimize_scalar

# Определяем функцию
def f(x1, x2):
    return 4 * x1**2 + 5 * x2**2 - 3 * x1 * x2 + 9 * x1 - 2 * x2 + 5

# Градиент функции
def grad_f(x1, x2):
    df_dx1 = 8 * x1 - 3 * x2 + 9  # Частная производная по x1
    df_dx2 = 10 * x2 - 3 * x1 - 2  # Частная производная по x2
    return np.array([df_dx1, df_dx2])

# Алгоритм наискорейшего спуска
def steepest_descent(f, grad_f, x0, epsilon=1e-6, max_iter=1000):
    """
    Метод наискорейшего спуска для минимизации функции.

    Параметры:
    - f: целевая функция
    - grad_f: градиент функции
    - x0: начальное приближение (numpy массив)
    - epsilon: точность
    - max_iter: максимальное количество итераций

    Возвращает:
    - Минимум функции и соответствующие значения переменных
    """
    x = x0
    for k in range(max_iter):
        grad = grad_f(x[0], x[1])  # Вычисляем градиент
        
        # Проверяем условие сходимости
        grad_norm = np.linalg.norm(grad)
        if grad_norm < epsilon:
            print(f"Сошлось за {k+1} итераций")
            return x, f(x[0], x[1])

        # Вычисляем направление спуска
        S_k = - grad_norm

        # Определяем функцию одномерной оптимизации
        def f_lambda(lmbd):
            x_new = x + lmbd * S_k
            return f(x_new[0], x_new[1])

        # Решаем задачу одномерной оптимизации по λ
        res = minimize_scalar(f_lambda)
        if not res.success:
            raise ValueError("Не удалось найти оптимальное значение λ")

        lambda_k = res.x  # Оптимальный шаг
        x = x + lambda_k * S_k  # Обновляем значение x

    #print("Достигнуто максимальное число итераций")
    return x, f(x[0], x[1])

# Начальное приближение
x0 = np.array([2, 3])  # Например, начальная точка (x1, x2) = (0, 0)

# Запуск метода наискорейшего спуска
result, f_min = steepest_descent(f, grad_f, x0)

print(f"Минимум функции достигается при x = {result}, значение f = {f_min}")


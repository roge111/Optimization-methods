import math

def f(x):
    return round(math.log(1 + x ** 2) - math.sin(x), 3)


def halfDivision(a, b, e):
    while b - a > 2*e:
        x1 = round((a + b - e)/2, 3)
        x2 = round((a + b + e)/2, 3)

        y1 = f(x1)
        y2 = f(x2)

        if y1 > y2:
            a = x1
        else:
            b = x2
    x_min = round((a + b)/2, 3)
    y_min = f(x_min)
    return x_min, y_min







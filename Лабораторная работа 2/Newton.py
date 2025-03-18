import math
import numpy as np

def f(x):
    return round(math.log(1 + x ** 2) - math.sin(x), 3)

def f1(x):
    return round((2*x)/(x**2 + 1) - math.cos(x), 3)
def f2(x):
    return round((2 * (1 - x**2))/(x**2 + 1)**2  - math.sin(x), 3)



def newton(a, b, e):
    x0 = (a+b)/2
    f1x =  f1(x0)
    f2x = f2(x0)
    x1 = round(x0 - f1x/f2x, 3)
    while abs(f1(x1)) > e:
        f1x =  f1(x1)
        f2x = f2(x1)
        x1 = round(x1 - f1x/f2x, 3)
    x_min = x1
    y_min = f(x_min)
    return x_min, y_min

    


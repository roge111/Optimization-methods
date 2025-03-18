import math

def f(x):
    return round(math.log(1 + x ** 2) - math.sin(x), 4)
def f1(x):
    return round((2*x)/(x**2 + 1) - math.cos(x), 4)

def hord(a, b, e):
    x = round(a - (f1(a)/(f1(a) - f1(b)))*(a - b), 4)
    fx = f(x)
    f1x = f1(x)
    if abs(f1x) <= e:
        
        return x, fx
    else:
        if f1x > 0:
            b = x
        else:
            a = x
        return hord(a, b, e)
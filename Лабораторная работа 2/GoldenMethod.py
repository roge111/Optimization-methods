import math
def f(x):
    return round(math.log(1 + x ** 2) - math.sin(x), 3)

def goldenMethod(a, b, e):
    k2 = round((5**0.5 -1)/2, 4 )
    k1 = 1 - k2

    x1 = round(a + k1*(b-a), 4)
    x2 = round(a + k2*(b-a), 3)

    f1 = f(x1)
    f2 = f(x2)

    while (b-a) >= e:
        if f1 < f2:
            b = x2
            x2 = x1
            f2= f1

            x1 = round(a + k1*(b-a), 4)
            f1 = f(x1)
        else:
            a = x1
            x1 = x2

            f1 = f2
            x2 =round(a + k2*(b-a), 4)
            f2 = f(x2)
        
    x_min =round( (a + b)/2, 3)
    y_min = f(x_min)
    return x_min, y_min
            





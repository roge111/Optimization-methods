import math
def f(x):
    return round(math.log(1 + x ** 2) - math.sin(x), 4)
#     # return 2*x**2 + 16/x

def replace(x1, x2, x3, x, x_2):
    x_arr = [x1,x2,x3, x_2]
    x2 = x
    x_arr.sort()
    for i, x_e in enumerate(x_arr):
        if x_e > x2:
            x1 = x_arr[i-1]
            x3 = x_e
            break
    return x1, x2, x3

def approxyQuadro(a, b, e1, e2, del_x):
    step = 1
    while step <= 8:
        if step == 1:
            x1 = float(input("Введите начально значение x1>> "))
        elif step == 2:
            x2 = x1 + del_x
        elif step == 3:
            f1 = f(x1)
            f2 = f(x2)
        elif step == 4:
            if f1 > f2:
                x3 = x1 + 2 * del_x
            else:
                x3 = x1 - del_x
        elif step == 5:
            f3 = f(x3)
        elif step == 6:
            f_min = min(f1, f2, f3)
            if f_min == f1:
                x_min = x1
            elif f_min == f2:
                x_min = x2
            else:
                x_min = x3
        elif step == 7:
            z = round((x2 - x3) * f1 + (x3 - x1) * f2 + (x1 - x2) * f3, 4)
            if z == 0:
                x1 = x_min
                step = 2
                continue
            x = round((1/2)*((x2**2 - x3**2)*f1 + (x3**2 - x1**2) * f2 + (x1**2 - x2**2) * f3)/z, 4)
            fx = f(x)
        else:
            
            if abs((f_min - fx)/fx) < e1 and abs((x_min - x)/x)<e2:
                return x, f(x)
            elif x >=min(x1, x2, x3) and x <= max(x1, x2, x3):
                if f_min <= fx:
                    x1, x2, x3 = replace(x1, x2, x3, x_min, x) #Идет замена на ближайшие от x две точки
                else:
                    x1, x2, x3 = replace(x1, x2, x3, x, x_min) #Идет замена на ближайшие от x две точки
                f1 = f(x1)
                f2 = f(x2)
                f3 = f(x3)
                step = 6
                continue
            else:
                x1 = x
                step = 2
                continue
            
        step += 1



e = float(input("Введите желаемую погрешность>> "))
print(approxyQuadro(0, round(math.pi/4, 4), e, 0.03, 1))
from scipy.optimize import fsolve

def f(x1, x2):
    return 4 * x1**2 + 5 * x2**2 - 3 * x1 * x2 + 9 * x1 - 2 * x2 + 5

def fp_x1(x1, x2): #Производная по x1
    return 8 * x1 - 3 * x2 + 9


def fp_x2 (x1, x2): #Производная по x2
    return 10 * x2 - 3 * x1 - 2

#Функция len_coor ищет расстояние между двумя точками по координатам
def len_coor(M, M_old):
    x = M[0]
    y = M[1]

    x_old = M_old[0]
    y_old = M_old[1]

    return ((x - x_old)**2 + (y - y_old)**2)**0.5


#Поиск экстремума
def coordinate_descent (x1, x2, max_step, e):
    begin = -1
    M_old = (0, 0)
    M = (x1, x2)
    fm = f(x1, x2)
    l = len_coor(M, M_old)
    step = 0
    while l > e and step <= max_step:
        #Минимизация по x1
        def equation_x1(x1):
            return fp_x1(x1, x2)
        x1 = float(fsolve(equation_x1, begin)[0])#Поиск корня для призводной по x2 приравненной к нулю. fslove - реализация метода Ньютона
        #Минимизация по x2
        def equation_x2(x2):
            return fp_x2(x1, x2)
        x2 = float(fsolve(equation_x2, begin)[0]) #Поиск корня для призводной по x2 приравненной к нулю. fslove - реализация метода Ньютона

        fm_old = fm
        fm = f(x1, x2)

        M_old = M
        M = (x1, x2)

        l = len_coor(M, M_old)
        step += 1

    return M, f(M[0], M[1])




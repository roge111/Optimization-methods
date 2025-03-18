import HalfDivision as hd
import GoldenMethod as gm
import HordMethod as hm
import Newton as nt
import math



a, b, e = input('Введите леву и правую граници отрезка и эпсила через пробел: ').split()
if 'pi/4' in a:
    a = math.pi/4
elif 'pi/4' in b:
    b = math.pi/4
a = float(a)
b = float(b)
e = float(e)


print("Посик минимум методом половинного деления")
print(f'Ваш результат: {hd.halfDivision(a, b, e)}')

print('Поиск минимума методом золотого сеченя')
print(f'Ваш результат: {gm.goldenMethod(a, b, e)}')

print('Поиск минимума методом Хорд')
print(f'Ваш результат: {hm.hord(a, b, e)}')

print('Поиск минимума с помощью Ньютона')
print(f'Ваш результат: {nt.newton(a, b, e)}')

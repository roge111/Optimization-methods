from sympy import symbols, diff, solve, Symbol
from math import cos
from sympy.abc import x

x = symbols('x')
a = float(x)
f = cos(a - 1) 
x0 = 1

dif = diff(f, x)

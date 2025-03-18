from scipy.optimize import fsolve
def f(x1):
    return 2 * x1 + 4.5

initial_guess = 1.0

root = fsolve(f, initial_guess)
print(root[0])
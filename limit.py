# %% imports
from sympy import *
init_printing()

# %% symbols
x = symbols('x')

# %% limit
# Exercicio 1
limit((x - 2) / (x ** 2 - 4), x, 2)


# Exercicio
# %% symbols
x = symbols('x')


# %% functions
def f(x):
    return ((x ** 2 + x - 6) / (x + 3))


f(x)
Limit(f(x), x, -3, dir="+")
Limit(f(x), x, -3, dir="+").doit()
Limit(f(x), x, -3, dir="-")
Limit(f(x), x, -3, dir="-").doit()

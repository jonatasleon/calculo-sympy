# %% imports
from sympy import *
init_printing()

# %% symbols
x = symbols('x')

# %% limit
# Exercicio 1
limit((x - 2) / (x ** 2 - 4), x, 2)


# Exercicio 2
# %% symbols
x, y, z, t = symbols('x y z t')
k, m, n = symbols('k m n', integer=True)
f, g, h = symbols('f g h', cls=Function)

# %% functions
def f(x):
    return ((x ** 2 + x - 6) / (x + 3))


f(800)
Limit(f(x), x, -3, dir="+")
Limit(f(x), x, oo, dir="-")
expr
expr.doit()

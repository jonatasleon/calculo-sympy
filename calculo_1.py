# %% import
from sympy import symbols, pi
from sympy.plotting import plot
import numpy as np
%matplotlib inline


# %% declara symbols
x, y = symbols('x y')


# %% declara função
def f(x):
    return x ** 2


step = 2.5
for i, v in enumerate(np.arange(-10, 11, step)):
    print('f(', v, ')', ' = ', f(v), sep='')

p1 = plot(f(x))

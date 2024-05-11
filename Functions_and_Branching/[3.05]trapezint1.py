# Exercise 3.5

from scipy.integrate import quad
from scipy import exp, pi, cos, sin, log

def trapezint1(f, a, b):
    return (b - a) / 2. * (f(a) + f(b))

f1 = [exp, 0, log(3)]
f2 = (cos, 0, pi)
f3 = (sin, 0, pi)
f4 = (sin, 0, pi / 2)

functions = [f1, f2, f3, f4]

def verify(f, a, b):
    exact = quad(f, a, b)[0]
    approx = trapezint1(f, a, b)
    error = abs(exact - approx)
    print('The exact integral of %s between %.5f and %.5f is %.5f. The approximate answer is %.5f giving an error of %.5f' % (f.__name__, a, b, exact, approx, error))

for f in functions:
    verify(f[0], f[1], f[2])

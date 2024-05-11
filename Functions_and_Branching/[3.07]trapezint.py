# Exercise 3.7

from scipy.integrate import quad
from scipy import exp, pi, cos, sin, log

def trapezint(f, a, b, n):
    s = (f(a) + f(b)) / 2
    h = (b - a) / float(n)
    for i in range(1, n):
        s += f(a + i * h)
    s *= h
    return s

f1 = [exp, 0, log(3)]
f2 = (cos, 0, pi)
f3 = (sin, 0, pi)
f4 = (sin, 0, pi / 2)

functions = [f1, f2, f3, f4]

def verify(f, a, b, n):
    exact = quad(f, a, b)[0]
    approx = trapezint(f, a, b, n)
    error = abs(exact - approx)
    print('The exact integral of %s between %.5f and %.5f is %.5f. The approximate answer is %.5f giving an error of %.5f' % (f.__name__, a, b, exact, approx, error))

for f in functions:
    verify(f[0], f[1], f[2], 10)

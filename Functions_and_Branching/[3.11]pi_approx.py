# Exercise 3.11

from math import sin, cos, pi, sqrt

def pathlength(x, y):
    L = 0
    for i in range(1, len(x)):
        dL_squared = (x[i] - x[i - 1]) ** 2 + (y[i] - y[i - 1]) ** 2
        L += sqrt(dL_squared)
    return L

def points(N):
    x = [0.5 * cos(2 * pi * i / N) for i in range(N + 1)]
    y = [0.5 * sin(2 * pi * i / N) for i in range(N + 1)]
    return x, y

N_list = [2 ** k for k in range(2, 11)]

for N in N_list:
    x, y = points(N)
    approx = pathlength(x, y)
    print('For {:4d} points on the circle, pi approximates to {:.8f} '
          'giving and error of {:.8f}'.format(N, approx, pi - approx))

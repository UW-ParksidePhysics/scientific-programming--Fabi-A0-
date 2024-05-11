# Exercise 3.13

from math import sin, pi

def S(t, n, T):
    s = 0
    for i in range(1, n + 1):
        s += 1.0 / (2 * i - 1) * sin(2 * (2 * i - 1) * pi * t / T)
    s *= 4 / pi
    return s

def f(t, T):
    if 0 < t < T / 2:
        ans = 1
    elif abs(t - T / 2) < 1E-14:
        ans = 0
    elif T / 2 < t < T:
        ans = -1
    else:
        print('Error: t must be between 0 and T')
        ans = None
    return ans

n_list = [1, 3, 5, 10, 30, 100]
alpha_list = (0.01, 0.25, 0.49)
T = 2 * pi
t_list = [2 * alpha * T for alpha in alpha_list]

for n in n_list:
    print(f'n = {n}')
    print(f'  Function t={0.01:.2f}*pi t={0.25:.2f}*pi t={0.49:.2f}*pi')
    print(f'{"f(t, T)":10s} {f(t_list[0], T):.7f} {f(t_list[1], T):.7f} {f(t_list[2], T):.7f}')
    print(f'{"S(t, n, T)":10s} {S(t_list[0], n, T):.7f} {S(t_list[1], n, T):.7f} {S(t_list[2], n, T):.7f}')
    print(f'{"Error":10s} {abs(S(t_list[0], n, T) - f(t_list[0], T)):.7f} {abs(S(t_list[1], n, T) - f(t_list[1], T)):.7f} {abs(S(t_list[2], n, T) - f(t_list[2], T)):.7f}')
    print()

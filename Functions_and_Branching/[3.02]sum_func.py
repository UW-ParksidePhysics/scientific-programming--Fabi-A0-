# Exercise 3.2

def sum_1_div_k(M=100):
    s = 0
    k = 1
    while k <= M:
        s += 1. / k
        k += 1
    print(s)

sum_1_div_k(3)
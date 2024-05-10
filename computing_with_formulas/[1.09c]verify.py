# Exercise 1.09c

a = 3.3
b = 5.3
a2 = a ** 2
b2 = b ** 2

eq1_sum = a2 + 2 * a * b + b2
eq2_sum = a2 - 2 * a * b + b2

eq1_pow = (a + b) ** 2
eq2_pow = (a - b) ** 2

print(f'First equation: {eq1_sum} = {eq1_pow}')
print(f'Second equation: {eq2_sum} = {eq2_pow}')

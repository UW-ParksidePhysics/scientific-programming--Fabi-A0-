# Exercise 2.15

from math import asin, pi

# Number of intervals between 0 and 1, inclusive.
n = 10
# Generate a list of n+1 evenly spaced values between 0 and 1, inclusive.
x_list = [i * 1. / n for i in range(n + 1)]

# Header for the output table.
print('------------------')
print('{:<3} {:>13}'.format('x', 'arcsin(x)'))

# Loop over each value in x_list to calculate its arcsin, converting the result to degrees.
for x in x_list:
    print('{:<3.2f} {:>12.2f}'.format(x, asin(x) * 180 / pi))

# Footer for the output table.
print('------------------')

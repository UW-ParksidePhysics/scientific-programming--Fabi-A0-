# Exercise 1.10

from math import pi, exp, sqrt

m = 0  # Mean of the distribution
s = 2.0  # Standard deviation of the distribution
x = 1.0  # Value at which the Gaussian function is evaluated

# Calculation of the Gaussian function
f = 1 / (sqrt(2 * pi) * s) * exp(-0.5 * ((x - m) / s) ** 2)
print(f) 
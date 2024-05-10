# Exercise 1.17

from cmath import sqrt

a = 2
b = 1
c = 2

# Calculate the discriminant
q = sqrt(b * b - 4 * a * c)

# Calculate the two solutions
x1 = (-b + q) / (2 * a)
x2 = (-b - q) / (2 * a)

# Print the solutions
print(x1)
print(x2)

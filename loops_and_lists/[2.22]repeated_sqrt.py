# Exercise 2.22: Numerical precision and rounding errors in repeated operations

from math import sqrt

# Loop over a range of iteration counts
for n in range(1, 60):
    r = 2.0  # Initial value
    # Apply the square root function n times
    for i in range(n):
        r = sqrt(r)
    # Square the result n times
    for i in range(n):
        r = r ** 2
    # Print the final result after n square roots followed by n squares
    print(f'{n} times sqrt and **2: {r:.16f}')

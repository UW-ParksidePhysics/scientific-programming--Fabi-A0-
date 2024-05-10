# Exercise 2.24: Comparing floating-point numbers

# First comparison: Direct equality check
a = 1 / 947.0 * 947
b = 1
if a != b:
    print('Wrong result! (Direct comparison)')

# Correct approach: Using a tolerance for floating-point comparison
a = 1 / 947.0 * 947
b = 1
if abs(a - b) > 1e-15:
    print('Wrong result! (Using tolerance)')

# This code highlights the importance of using a tolerance when comparing floating-point numbers
# to account for potential precision errors.

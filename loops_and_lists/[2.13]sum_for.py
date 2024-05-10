# Exercise 2.13


s = 0
# Set the maximum value of the sequence to 100.
M = 100

# Iterate over a sequence of numbers from 1 to M inclusive.
for k in range(1, M + 1):
    # For each k, add the reciprocal of k to the sum.
    s += 1. / k

# Print the final sum of the series.
print(s)

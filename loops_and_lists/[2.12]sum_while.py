# Exercise 2.12


s = 0
# Initialize the counter variable, k, to 1. This will track our current position in the sequence.
k = 1
# Set the maximum value of the sequence to 100.
M = 100

# Loop until k exceeds M.
while k <= M:
    # Add the reciprocal of k to the sum.
    s += 1. / k
    # Increment k to move to the next number in the sequence.
    k += 1

# Print the calculated sum of the series.
print(s)

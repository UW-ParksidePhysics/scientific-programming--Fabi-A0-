# Exercise 2.11: Generate and Print a Sequence of Numbers Using List Comprehension


h = 0.01  # Increment
# Generate the sequence of numbers using list comprehension
x = [1 + i * h for i in range(0, 101)]

# Print the generated sequence
for xval in x:
    print('{:3.2f}'.format(xval), end=' ')  # Print each value formatted to two decimal places, on the same line

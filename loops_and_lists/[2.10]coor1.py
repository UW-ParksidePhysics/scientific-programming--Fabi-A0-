# Exercise 2.10: Generate and Print a Sequence of Numbers


h = 0.01  # Increment
x = []  # Initialize list to store numbers

# Generate the sequence of numbers
for i in range(0, 101):
    x.append(1 + i * h)  # Append each incremented value to the list

# Print the generated sequence
for xval in x:
    print('{:3.2f}'.format(xval), end=' ')  # Print each value formatted to two decimal places, on the same line

# Exercise 2.04: Generate and Print Odd Numbers Using a List

n = 12  # Upper limit for generating odd numbers
i = 0  # Initialize counter
odd_nos = []  # Initialize list to store odd numbers

# Loop to generate odd numbers and store them in the list
while i < int(round(n / 2.)):
    odd_nos.append(2 * i + 1)  # Calculate the next odd number and add it to the list
    i += 1  # Increment the counter

# Print each odd number from the list
for no in odd_nos:
    print(no, end=' ')  # Print the odd number, keeping them on the same line

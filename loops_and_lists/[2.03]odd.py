# Exercise 2.03: Generate and Print Odd Numbers
# This program prints all odd numbers up to a specified limit.

n = 12  # Specify the upper limit for generating odd numbers
i = 0  # Initialize counter

# Loop to generate and print odd numbers
while i < int(round(n / 2.)):
    print(2 * i + 1, end=' ')  # Calculate and print the next odd number
    i += 1  # Increment the counter

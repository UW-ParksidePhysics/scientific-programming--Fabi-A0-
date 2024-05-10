# Exercise 2.08: Working with a List of Prime Numbers


# Initialize a list with prime numbers
primes = [2, 3, 5, 7, 11, 13]

# Print the initial list of prime numbers
for prime in primes:
    print(prime, end=' ')  # Ensure numbers are printed on the same line

# Add another prime number to the list
p = 17
primes.append(p)

print('\n')  # Print a newline for better readability between the lists

# Print the updated list of prime numbers
for prime in primes:
    print(prime, end=' ')  # Ensure numbers are printed on the same line

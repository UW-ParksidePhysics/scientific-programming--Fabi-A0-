# Exercise 2.05: Generate and Print Odd Numbers Using List Comprehension

n = 12  # Upper limit for generating odd numbers

# Generate odd numbers using list comprehension and store them in odd_nos
odd_nos = [2 * i + 1 for i in range(0, int(round(n / 2.)))]

# Iterate through the list and print each odd number
for no in odd_nos:
    print(no, end=' ')  # Print the odd number, keeping them on the same line

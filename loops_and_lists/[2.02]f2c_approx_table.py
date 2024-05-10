# Exercise 2.02: Enhanced Fahrenheit to Celsius Conversion Table with Approximation
# This program generates a table converting temperatures from Fahrenheit to Celsius

print('------------------------')  # Print the start of the table

F = 0  # Initialize Fahrenheit temperature at 0
dC = 10  # Increment of Fahrenheit temperature in the loop

# Print column headers for Fahrenheit, exact Celsius, and approximate Celsius values
print('%6s %8s %8s' % ('F', 'C', '~C'))

# Loop to generate and print conversion values and their approximations
while F <= 100:  # Continue loop until Fahrenheit reaches 100
    C = (5.0 / 9) * (F - 32)  # Convert Fahrenheit to exact Celsius
    C_approx = 0.5 * (F - 30)  # Calculate approximate Celsius
    print('%6.2f %8.2f %8.2f' % (F, C, C_approx))  # Print current Fahrenheit, exact and approximate Celsius
    F = F + dC  # Increment the Fahrenheit value

print('------------------------')  # End of the table

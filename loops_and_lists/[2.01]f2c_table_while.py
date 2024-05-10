# Exercise 2.01: Fahrenheit to Celsius Conversion Table
# This program generates a table converting temperatures from Fahrenheit to Celsius.

print('------------------')   # Print the start of the table

F = 0   # Initialize Fahrenheit temperature at 0
dC = 10  # Increment of Fahrenheit temperature in the loop

# Print column headers
print('%6s %8s' % ('F', 'C'))

# Loop to generate and print conversion values from Fahrenheit to Celsius
while F <= 100:  # Continue loop until Fahrenheit reaches 100
    C = (5.0 / 9) * (F - 32)  # Convert Fahrenheit to Celsius
    print('%6.2f %8.2f' % (F, C))  # Print the current Fahrenheit and its Celsius conversion
    F = F + dC  # Increment the Fahrenheit value

print('------------------')  # End of the table

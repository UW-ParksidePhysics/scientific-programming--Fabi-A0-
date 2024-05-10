# Exercise 2.18: Temperature conversion using lists

# Creating a list of Fahrenheit values starting from 0 to 100 in steps of 10
Fahrenheit_values = [i for i in range(0, 110, 10)]

# Converting Fahrenheit to Celsius using the exact formula
Celsius_exact = [(5.0 / 9) * (f - 32) for f in Fahrenheit_values]

# Approximating the Celsius conversion using a simplified formula
Celsius_approx = [0.5 * (f - 30) for f in Fahrenheit_values]

# Combining the Fahrenheit, exact Celsius, and approximate Celsius values for tabular display
temperature_conversion_table = [[f, c_exact, c_approx] for f, c_exact, c_approx in zip(Fahrenheit_values, Celsius_exact, Celsius_approx)]

# Printing the table headers
print('------------------------')
print(f'{"F":>6} {"C":>8} {"~C":>8}')

# Printing each row of the table
for f, c_exact, c_approx in temperature_conversion_table:
    print(f'{f:6.2f} {c_exact:8.2f} {c_approx:8.2f}')

print('------------------------')

# Exercise 2.14

# Initial amount of the investment.
initial_amount = 100
# Annual interest rate as a percentage (e.g., 5.5%).
p = 5.5  
# Variable to keep track of the current amount of the investment.
amount = initial_amount
# Counter for the number of years passed.
years = 0

# Loop until the current amount exceeds 1.5 times the initial amount.
while amount <= 1.5 * initial_amount:
    # Increase the amount by the interest accrued in one year.
    amount += p / 100 * initial_amount
    # Increment the year counter.
    years += 1

# Print the total number of years required to reach the target amount.
print(years)

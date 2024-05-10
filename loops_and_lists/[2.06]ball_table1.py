# Exercise 2.06: Vertical Position of a Ball Over Time

v0 = 1  # Initial velocity of the ball (m/s)
g = 9.81  # Acceleration due to gravity (m/s^2)
n = 11  # Number of points in the table

# Calculate time interval between each point
dt = 2 * v0 / g / (n - 1)

# Print table headers for time (t) and vertical position (y)
print('%6s %6s' % ('t', 'y'))

# Generate and print the table of times and vertical positions
for i in range(0, n):
    t = i * dt  # Calculate time at each point
    y = v0 * t - 0.5 * g * t ** 2  # Calculate vertical position at each time point
    print('%6.3f %6.3f' % (t, y))  # Print the time and vertical position

# Exercise 2.07: Vertical Position of a Ball Over Time Using List Comprehension

v0 = 10  # Initial velocity of the ball (m/s)
g = 9.81  # Acceleration due to gravity (m/s^2)
n = 81  # Number of points in the table

# Calculate time interval between each point
dt = 2 * v0 / g / (n - 1)

# Generate lists of time intervals and vertical positions using list comprehension
t = [i * dt for i in range(n)]  # Time intervals
y = [v0 * t[i] - 0.5 * g * t[i] ** 2 for i in range(n)]  # Vertical positions

# Print table headers for time (t) and vertical position (y)
print('%6s %6s' % ('t', 'y'))

# Print each time and corresponding vertical position
for tval, yval in zip(t, y):
    print('%6.3f %6.3f' % (tval, yval))

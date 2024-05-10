# Exercise 2.19: Ball trajectory table

# Initial conditions and constants
initial_velocity = 10  # Initial velocity of the ball in meters/second
g = 9.81  # Acceleration due to gravity in meters/second^2
n = 81  # Number of points
time_interval = 2 * initial_velocity / g / (n - 1)  # Time interval between points

# Generating time points
time_points = [i * time_interval for i in range(n)]
# Calculating positions at each time point
positions = [initial_velocity * t - 0.5 * g * t ** 2 for t in time_points]

# Method 1: Using separate lists for time and position
print(f'{"t":>6} {"y":>6}')
for i in range(len(time_points)):
    print(f'{time_points[i]:6.3f} {positions[i]:6.3f}')

# Method 2: Using a list of tuples for time and position pairs
time_position_pairs = [[t, y] for t, y in zip(time_points, positions)]

print(f'{"t":>6} {"y":>6}')
for t, y in time_position_pairs:
    print(f'{t:6.3f} {y:6.3f}')

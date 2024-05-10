# Exercise 2.20: Squaring list elements with for-loop vs list comprehension

# Generate a list of radii using a for-loop
radii_list = []
for i in range(5):
    radii_list.append(10 ** i)

# Calculate the squares of radii using a traditional for-loop
squared_radii_for_loop = []
for radius in radii_list:
    squared_radii_for_loop.append(radius ** 2)

# Calculate the squares of radii using a list comprehension within a list comprehension
squared_radii_list_comp = [radius ** 2 for radius in [10 ** i for i in range(5)]]

# Check if the two methods produce the same result
print(f"Equality of results: {squared_radii_for_loop == squared_radii_list_comp}")

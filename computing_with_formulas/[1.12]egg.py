# Exercise 1.12

from math import log, pi

# Constants
rho = 1.038 * 1000  # Egg density (kg m^-3)
c = 3.7 * 1000  # Specific heat capacity (J kg^-1 K^-1)
K = 0.54  # Thermal conductivity (W m^-1 K^-1)
T_w = 373.15  # Boiling water temperature (K)
T_y = 343.15  # Desired yolk temperature (K)

# Function to calculate cooking time
def cooking_time(T_0, M):
    return M ** (2.0 / 3) * c * rho ** (1.0 / 3) / (K * pi ** 2 * (4 * pi / 3) ** (2.0 / 3)) * log(0.76 * (T_0 - T_w) / (T_y - T_w)) / 60

# Cooking times for eggs from the fridge
T_0_fridge = 277.15  # Starting temperature from fridge (K)
small_egg_fridge = cooking_time(T_0_fridge, 0.047)  # Small egg mass
large_egg_fridge = cooking_time(T_0_fridge, 0.067)  # Large egg mass

# Cooking times for eggs at room temperature
T_0_room = 293.15  # Starting temperature from room (K)
small_egg_room = cooking_time(T_0_room, 0.047)  # Small egg mass
large_egg_room = cooking_time(T_0_room, 0.067)  # Large egg mass

# Print the results
print(f'From the fridge: to hard boil a small egg cook for {small_egg_fridge:.2f} minutes and a large egg for {large_egg_fridge:.2f} minutes.')
print(f'At room temperature: to hard boil a small egg cook for {small_egg_room:.2f} minutes and a large egg for {large_egg_room:.2f} minutes.')

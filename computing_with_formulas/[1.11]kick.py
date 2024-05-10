# Exercise 1.11

from math import pi

C_D = 0.2  # Drag coefficient
rho = 1.2  # Density of air (kg m^-3)
A = pi * 0.11 ** 2  # Football cross-sectional area (m^2)
m = 0.43  # Football mass (kg)
g = 9.81  # Gravitational acceleration (ms^-1)

F_g = m * g  # Gravitational force

speed_conversion = 1000.0 / 3600  # Conversion factor from km/h to m/s

# Hard kick velocity and forces calculation
V = 120 * speed_conversion  # Hard kick velocity (m/s)
F_d = 0.5 * C_D * rho * A * V ** 2  # Drag force for hard kick
print(f'For a hard kick (v = {V}), the gravitational force is {F_g} and the drag force is {F_d}')

# Soft kick velocity and forces calculation
V = 10 * speed_conversion  # Soft kick velocity (m/s)
F_d = 0.5 * C_D * rho * A * V ** 2  # Drag force for soft kick
print(f'For a soft kick (v = {V}), the gravitational force is {F_g} and the drag force is {F_d}')

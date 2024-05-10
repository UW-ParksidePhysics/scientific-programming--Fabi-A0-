import numpy as np

# Constants
L = 1  # Length of the box in 1D
Lx, Ly = 1, 1  # Length of the box along x and y in 2D

# 1D Wave function
def psi_n(x, n):
    constant = np.sqrt(2 / L)
    sin_part = np.sin(n * np.pi * x / L)
    wave_function = constant * sin_part
    return wave_function

# 1D Probability density
def rho_n(x, n):
    probability_density = psi_n(x, n) ** 2
    return probability_density

# 2D Wave function
def psi_n_m(x, y, n, m):
    constant = 2 / np.sqrt(Lx * Ly)
    sin_part_x = np.sin(n * np.pi * x / Lx)
    sin_part_y = np.sin(m * np.pi * y / Ly)
    wave_function_2d = constant * sin_part_x * sin_part_y
    return wave_function_2d

# 2D Probability density
def rho_n_m(x, y, n, m):
    probability_density_2d = psi_n_m(x, y, n, m) ** 2
    return probability_density_2d
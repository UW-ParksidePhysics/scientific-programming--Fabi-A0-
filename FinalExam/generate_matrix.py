import numpy as np

def generate_matrix(minimum_x, maximum_x, number_of_dimensions, potential_name, potential_parameter):
    
    """
    Generates an NxN Hamiltonian matrix for a one-dimensional potential on a spatial grid.
    """

    hbar = 1.0  # Planck's constant over 2*pi in atomic units
    mass = 1.0  # Mass of the particle in atomic units

    # Calculate grid spacing
    grid_spacing = (maximum_x - minimum_x) / (number_of_dimensions - 1)
    diagonal = np.zeros(number_of_dimensions)
    off_diagonal = -0.5 * (hbar ** 2 / mass / grid_spacing ** 2) * np.ones(number_of_dimensions - 1)

    # Compute potential
    x = np.linspace(minimum_x, maximum_x, number_of_dimensions)
    if potential_name == 'harmonic':
        potential = 0.5 * mass * (potential_parameter * x**2)
    elif potential_name == 'sinusoidal':
        potential = potential_parameter * np.sin(np.pi * x / (maximum_x - minimum_x))
    elif potential_name == 'square':
        potential = np.zeros(number_of_dimensions)
        mid_point = number_of_dimensions // 2
        potential[:mid_point] = potential_parameter
        potential[mid_point:] = potential_parameter

    # Hamiltonian matrix assembly
    diagonal += potential
    matrix = np.diag(diagonal) + np.diag(off_diagonal, k=1) + np.diag(off_diagonal, k=-1)

    return matrix

if __name__ == "__main__":
    # Example usage
    matrix = generate_matrix(-1, 1, 100, 'harmonic', 1.0)
    print("Generated Hamiltonian Matrix:\n", matrix)

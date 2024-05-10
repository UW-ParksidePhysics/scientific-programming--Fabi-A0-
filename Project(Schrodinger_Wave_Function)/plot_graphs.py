import matplotlib.pyplot as plt
from quantum_formulas import psi_n, rho_n, psi_n_m, rho_n_m
import numpy as np

# Function to plot 1D quantum states for multiple n values
def plot_quantum_states(n_values):
    plt.ion() # Turn on interactive mode
    x_values = np.linspace(0, 1, 1000)  # Generate 1000 points between 0 and 1
    plt.figure(figsize=(10, 5))  # Set the figure size
    for n in n_values:  # Loop over each n value
        psi_values = psi_n(x_values, n)  # Calculate the wave function values
        rho_values = rho_n(x_values, n)  # Calculate the probability density values
        plt.plot(x_values, psi_values, label=f'ψ{n}(x)')  # Plot the wave function
        plt.plot(x_values, rho_values, '--', label=f'ρ{n}(x)', alpha=0.7)  # Plot the probability density
    plt.xlabel('x')  # Label the x-axis
    plt.ylabel('Function value')  # Label the y-axis
    plt.title(f'1D Wave Functions and Probability Densities for n = {n_values} ')
    plt.legend()  # Display a legend
    plt.grid(True)  # Display a grid
    plt.show()  # Show the plot and pause until the user closes the window
    plt.pause(0.001)  # Pause for a short time to allow the plot to update
    input(f"Press Enter to close graph for ψ(x) and ρ(x) for n = {n_values}")  # Wait for user input
    plt.close()  # Close the current plot window


# Function to plot 2D quantum states for given n, m values
def plot_quantum_states_2D(n, m):
    plt.ion() # Turn on interactive mode
    x_values = np.linspace(0, 1, 100)  # Generate 100 points between 0 and 1 for x
    y_values = np.linspace(0, 1, 100)  # Generate 100 points between 0 and 1 for y
    X, Y = np.meshgrid(x_values, y_values)  # Create a meshgrid for x and y values
    Z_psi = psi_n_m(X, Y, n, m)  # Calculate the wave function values
    Z_rho = rho_n_m(X, Y, n, m)  # Calculate the probability density values

    fig, ax = plt.subplots(1, 2, figsize=(10, 5))  # Create subplots for wave function and probability density

    # Plot the 2D wave function
    psi_contour = ax[0].contourf(X, Y, Z_psi, cmap='viridis')
    fig.colorbar(psi_contour, ax=ax[0], label='ψ value')
    ax[0].set_title(f'2D Wave Function ψ({n},{m})')
    ax[0].set_xlabel('x')
    ax[0].set_ylabel('y')

    # Plot the 2D probability density
    rho_contour = ax[1].contourf(X, Y, Z_rho, cmap='plasma')
    fig.colorbar(rho_contour, ax=ax[1], label='ρ value')
    ax[1].set_title(f'2D Probability Density ρ({n},{m})')
    ax[1].set_xlabel('x')
    ax[1].set_ylabel('y')

    plt.tight_layout()  # Adjust layout
    plt.show()  # Show the plot and pause until the user closes the window
    plt.pause(0.001)  # Pause for a short time to allow the plot to update
    input(f"Press Enter to close graph for ψ{n}{m}(x, y) and ρ{n}{m}(x, y) for n = {n} and m = {m}")  # Wait for user input
    plt.close() # Close the plot window
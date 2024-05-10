import numpy as np
import matplotlib.pyplot as plt


from datetime import datetime
from scipy.optimize import curve_fit
from numpy.linalg import eigh

from convert_units import convert_units
from equations_of_state import murnaghan
from generate_matrix import generate_matrix


def parse_file_name(filename):
    # Assuming filename format "ChemicalSymbol.CrystalSymmetry.Acronym.data"
    parts = filename.split('.')
    chemical_symbol = parts[0]
    crystal_symmetry = parts[1]
    approximation_acronym = parts[2]
    return chemical_symbol, crystal_symmetry, approximation_acronym
def read_two_columns_text(filename):
    data = np.loadtxt(filename)
    return data[:, 0], data[:, 1]  # Assuming volume is column 0, energy is column 1
def fit_eos(volumes, energies, initial_guess):
    from scipy.optimize import curve_fit
    from equations_of_state import murnaghan

    # Using curve_fit to fit the Murnaghan EOS to the data
    popt, pcov = curve_fit(murnaghan, volumes, energies, p0=initial_guess)
    return popt  # This contains the fitted parameters for the Murnaghan equation


def calculate_converted_units(value, from_unit, to_unit):
    return convert_units(value, from_unit, to_unit)
def plot_data_and_fit(volumes, energies, fit_curve):
    plt.figure()
    plt.plot(volumes, fit_curve, 'k-', label='Fit')
    plt.scatter(volumes, energies, color='b', label='Data')
    plt.xlabel('Volume ($Å^3$/atom)')
    plt.ylabel('Energy (eV/atom)')
    plt.legend()
    plt.show()

def plot_eigenvectors(x, eigenvectors, eigenvalues):
    plt.figure()
    for i, vec in enumerate(eigenvectors.T):
        plt.plot(x, vec, label=f'$\psi_{i+1}$, $E={eigenvalues[i]:.3f}$ a.u.')
    plt.axhline(0, color='black', linewidth=1)
    plt.xlabel('$x$ [a.u.]')
    plt.ylabel('$\psi_n(x)$ [a.u.]')
    plt.title('Selected Wavefunctions')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    filename = 'C.Fd-3m.GGA-PBE.volumes_energies_-986055706.dat'
    volumes, energies = read_two_columns_text(filename)
    chem_symbol, crystal_sym, approx_acronym = parse_file_name(filename)
    
    # Initial guess from quadratic fit
    quadratic_coeff = np.polyfit(volumes, energies, 2)  # A, B, C of Ax^2 + Bx + C
    # Assume some initial guesses for bulk modulus and its derivative
    initial_guess = [-quadratic_coeff[2], 1, 4, 75]  # E0, K0, K0', V0

    # Fit using the Murnaghan equation of state
    murnaghan_params = fit_eos(volumes, energies, initial_guess)
    fit_curve = murnaghan(volumes, *murnaghan_params)
    
    plot_data_and_fit(volumes, energies, fit_curve)
    
    matrix = generate_matrix(-10, 10, 110, 'harmonic', 100)
    eigenvalues, eigenvectors = eigh(matrix)
    x = np.linspace(-10, 10, 110)
    plot_eigenvectors(x, eigenvectors[:, :3], eigenvalues[:3])
    
    display_graph = True
    if display_graph:
        plt.show()
    else:
        plt.savefig('output_filename.png')




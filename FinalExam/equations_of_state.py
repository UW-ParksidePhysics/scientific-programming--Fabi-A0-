import numpy as np

def murnaghan(volumes, equilibrium_energy, bulk_modulus, bulk_modulus_derivative, equilibrium_volume):
   
    """
    Murnaghan equation of state.
    """
    

    k0pm1 = bulk_modulus_derivative - 1
    volumes_ratio = volumes / equilibrium_volume
    energy = equilibrium_energy + bulk_modulus * equilibrium_volume * (
             (1 / (bulk_modulus_derivative * k0pm1)) * np.power(volumes_ratio, -k0pm1) +
             volumes_ratio / bulk_modulus_derivative - 1 / k0pm1)
    return energy

def birch_murnaghan(volumes, equilibrium_energy, bulk_modulus, bulk_modulus_derivative, equilibrium_volume):
    
    """
    Birch-Murnaghan equation of state.
    """
    
    eta = (volumes / equilibrium_volume) ** (1/3)
    eta2 = eta * eta
    eta6 = eta2 * eta2 * eta2
    energy = equilibrium_energy + 9 * bulk_modulus * equilibrium_volume / 16 * (
             ((eta2 - 1)**3 * bulk_modulus_derivative) + 
             ((eta2 - 1)**2 * (6 - 4 * eta2)))
    return energy

def vinet(volumes, equilibrium_energy, bulk_modulus, bulk_modulus_derivative, equilibrium_volume):
   
    """
    Vinet equation of state.
    """
    
    x = (volumes / equilibrium_volume) ** (1/3)
    xi = 1.5 * (bulk_modulus_derivative - 1) * (1 - x)
    energy = equilibrium_energy + 2 * bulk_modulus * equilibrium_volume / (bulk_modulus_derivative - 1) ** 2 * \
             (2 - (3 * x - 2) * np.exp(xi))
    return energy

if __name__ == "__main__":
    # Example usage:
    volumes = np.linspace(50, 100, 100)
    equilibrium_energy = -50
    bulk_modulus = 0.5
    bulk_modulus_derivative = 4
    equilibrium_volume = 75

    energies_murnaghan = murnaghan(volumes, equilibrium_energy, bulk_modulus, bulk_modulus_derivative, equilibrium_volume)
    energies_birch = birch_murnaghan(volumes, equilibrium_energy, bulk_modulus, bulk_modulus_derivative, equilibrium_volume)
    energies_vinet = vinet(volumes, equilibrium_energy, bulk_modulus, bulk_modulus_derivative, equilibrium_volume)

   

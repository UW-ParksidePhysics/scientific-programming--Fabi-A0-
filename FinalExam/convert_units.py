import scipy.constants as const

def convert_units(value, from_units, to_units):
   
    """
    Convert the value from one unit system to another.
    """

    # Define conversions from atomic units to standard units
    if from_units == "cubic bohr per atom" and to_units == "cubic angstroms per atom":
        # 1 bohr^3 = 0.14818471147216278 Å^3
        return value * 0.14818471147216278
    elif from_units == "rydberg per atom" and to_units == "electron volts per atom":
        # 1 rydberg = 13.605693122994 eV
        return value * 13.605693122994
    elif from_units == "rydberg per cubic bohr" and to_units == "gigapascals":
        # Conversion factor for pressure
        return value * 14710.507848260711
    else:
        raise ValueError(f"Unsupported unit conversion from {from_units} to {to_units}")

if __name__ == "__main__":
    # Example conversions to test if the module works correctly
    print("1 cubic bohr per atom to cubic angstroms per atom:", convert_units(1, "cubic bohr per atom", "cubic angstroms per atom"))
    print("1 rydberg per atom to electron volts per atom:", convert_units(1, "rydberg per atom", "electron volts per atom"))
    print("1 rydberg per cubic bohr to gigapascals:", convert_units(1, "rydberg per cubic bohr", "gigapascals"))

from quantum_formulas import psi_n, rho_n, psi_n_m, rho_n_m
from plot_graphs import plot_quantum_states, plot_quantum_states_2D
from user_input import handle_user_input

def main():
    # This function will start the process of handling user input and responding accordingly.
    handle_user_input()

# This conditional ensures that main() is called only when this script is executed directly,
# and not when it is imported as a module in another script.
if __name__ == "__main__":
    main()
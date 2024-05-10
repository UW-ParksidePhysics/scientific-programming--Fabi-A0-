from plot_graphs import plot_quantum_states, plot_quantum_states_2D

def handle_user_input():
  while True:  # Start an infinite loop
    # Ask the user to choose between 1D and 2D models
    dimension = input("Choose the model dimension (1D or 2D): ").strip().lower()

    if dimension == '1d':
        # For the 1D model, ask for a series of quantum numbers separated by commas
        n_input = input("Enter the quantum numbers n separated by commas (e.g., 1,2,3): ")
        try:
            # Convert the input string into a list of integers
            n_values = [int(n.strip()) for n in n_input.split(',')]
            # Check if any of the input numbers are less than 1
            if any(n < 1 for n in n_values):
                print("Please enter positive integers only.")
            else:
                # If the input is valid, plot the quantum states for the provided n values
                plot_quantum_states(n_values)
        except ValueError:
            # If the conversion fails, inform the user of invalid input
            print("Invalid input. Please enter positive integers separated by commas.")

    elif dimension == '2d':
        try:
            # For the 2D model, ask for quantum numbers n and m
            n = int(input("Enter the quantum number n: "))
            m = int(input("Enter the quantum number m: "))
            # Check if n or m is less than 1
            if n < 1 or m < 1:
                print("Please enter positive integers only for both n and m.")
            else:
                # If the input is valid, plot the quantum states for the provided n and m values
                plot_quantum_states_2D(n, m)
        except ValueError:
            # If the conversion fails, inform the user of invalid input
            print("Invalid input. Please enter positive integers for n and m.")

    else:
        # If the dimension input doesn't match '1d' or '2d', inform the user
        print("Invalid selection. Please enter '1D' for one dimension or '2D' for two dimensions.")

    # Ask the user if they want to continue or exit
    choice = input("Do you want to continue? (y/n): ").strip().lower()
    if choice != 'y':
        break  # Exit the loop if the user doesn't want 
    


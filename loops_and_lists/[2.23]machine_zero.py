# Exercise 2.23: Finding the machine epsilon

# Initialize eps to 1.0
eps = 1.0
# Loop until 1.0 + eps is indistinguishable from 1.0
while 1.0 != 1.0 + eps:
    print(f'............... {eps}')
    eps /= 2.0  # Halve eps to find the smallest number that affects the sum

# Print the final eps when 1.0 + eps is no longer different from 1.0
print(f'final eps: {eps}')

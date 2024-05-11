# Exercise 3.1

def C(F):
    C_val = (5. / 9) * (F - 32)
    F_val = (9.0 / 5) * C_val + 32
    return C_val if abs(F_val - F) < 1E-12 else 'Error'

print(C(30))

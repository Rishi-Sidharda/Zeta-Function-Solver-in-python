# NOTE
# DUE TO NUMERICAL PRECISION LIMITATIONS ANY OUTPUT THAT IS LESS THAN 10^-20 IS CONSIDERED A ZERO

import sympy as sp

# Define the variables
s = sp.symbols('s', complex=True)

# Define the Riemann zeta function and the Gamma function

zeta = sp.functions.special.zeta_functions.zeta
gamma = sp.gamma

# Define the functional equation of the Riemann zeta function


def zeta_functional_equation(s):
    return 2**s * sp.pi**(s - 1) * sp.sin(sp.pi * s / 2) * gamma(1 - s) * zeta(1 - s)

# Function to evaluate the functional equation for a given complex number


def evaluate_functional_equation(complex_val):
    lhs = zeta(complex_val)
    rhs = zeta_functional_equation(complex_val)
    rhs_simplified = sp.simplify(rhs)
    return lhs, rhs, rhs_simplified


# Input: complex number
s_val = sp.sympify('0.5 + 14.1347251417346937904572519835625*I')

# Evaluate the functional equation for the complex input
lhs, rhs, rhs_simplified = evaluate_functional_equation(s_val)

# Print the results
print(f"zeta({s_val}) = {lhs}")
# print(f"Functional equation at s = {s_val}: {rhs}")
print(f"Simplified RHS: {rhs_simplified}")

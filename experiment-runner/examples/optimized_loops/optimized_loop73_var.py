import sys
import time
import random
import numpy as np  # NumPy for matrix multiplication
from pyJoules.energy_meter import measure_energy

# Generate a large stack of random operators and parentheses
def generate_large_stack(size):
    operators = ['+', '-', '*', '/']
    parentheses = ['(', ')']
    stack = []
    for _ in range(size):
        # Randomly choose from operators and parentheses
        stack.append(random.choice(operators + parentheses))
    return stack

@measure_energy
def var_termination_loop(stack, post_fix):
    termination_value = '('  # Cache the termination condition
    while stack and stack[-1] != termination_value:
        post_fix.append(stack.pop())

        # Heavy computation: Matrix multiplication for energy consumption
        matrix_a = np.random.rand(100, 100)
        matrix_b = np.random.rand(100, 100)
        result = np.dot(matrix_a, matrix_b)

        # Additional heavy computation
        matrix_c = np.random.rand(100, 100)
        matrix_d = np.random.rand(100, 100)
        result = np.dot(matrix_c, matrix_d)

# Example setup
stack = generate_large_stack(10000)  # Generate a large stack with 10,000 elements
post_fix = []

var_termination_loop(stack, post_fix)

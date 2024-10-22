import sys
import time
import random
import numpy as np  # Import NumPy for matrix multiplication
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
def early_termination_loop(stack, post_fix, priority, x):
    while stack and stack[-1] != '(' and priority[x] <= priority[stack[-1]]:
        post_fix.append(stack.pop())

        if random.randint(0, 100) < 10:  # Early exit condition
            break

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
priority = {'+': 1, '*': 2, '(': 0, ')': 0}  # Added priorities for parentheses
x = '+'

early_termination_loop(stack, post_fix, priority, x)

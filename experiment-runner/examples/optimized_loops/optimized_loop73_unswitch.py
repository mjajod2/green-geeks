import sys
import time
import numpy as np
from pyJoules.energy_meter import measure_energy
import random


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
def unswitched_loop(stack, post_fix):
    while stack and stack[-1] != '(':
        post_fix.append(stack.pop())

        # Heavy computation
        matrix_c = np.random.rand(100, 100)
        matrix_d = np.random.rand(100, 100)
        result = np.dot(matrix_c, matrix_d)
        large_computation = sum(random.randint(1, 1000000) ** 2 for _ in range(1000))

# Example setup
stack = generate_large_stack(10000)  # Generate a large stack with 10,000 elements
post_fix = []

unswitched_loop(stack, post_fix)

import sys
import time
import random
import numpy as np  # NumPy for matrix multiplication
from pyJoules.energy_meter import measure_energy

@measure_energy
def unswitched_loop(stack, post_fix, priority, x):
    termination_check = '('  # Cache condition outside loop
    priority_x = priority[x]
    while stack and stack[-1] != termination_check and priority_x <= priority.get(stack[-1], float('inf')):
        post_fix.append(stack.pop())

        # Heavy computation: Matrix multiplication for energy consumption
        matrix_a = np.random.rand(100, 100)
        matrix_b = np.random.rand(100, 100)
        result = np.dot(matrix_a, matrix_b)

# Example setup
def generate_large_stack(size):
    operators = ['+', '-', '*', '/']
    parentheses = ['(', ')']
    stack = []
    for _ in range(size):
        stack.append(random.choice(operators + parentheses))
    return stack

stack = generate_large_stack(10000)  # Generate a large stack with 10,000 elements
post_fix = []
priority = {'+': 1, '*': 2, '(': 0, ')': 0}  # Added '(' and ')' to the priority dictionary
x = '+'

unswitched_loop(stack, post_fix, priority, x)

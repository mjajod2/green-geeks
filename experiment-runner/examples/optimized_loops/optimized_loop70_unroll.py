import sys
import time
from pyJoules.energy_meter import measure_energy
import random

@measure_energy
def unrolled_loop(equation, operand_stack, operator_stack, operators):
    for i in range(0, len(equation), 2):  # Unrolling two iterations at once
        # First unrolled iteration
        item = equation[i]
        if item.isdigit():
            operand_stack.append(int(item))
        elif item in operators:
            operator_stack.append(item)

        # Simulated additional computation
        large_computation = sum(random.randint(1, 1000000) ** 2 for _ in range(1000))

        # Second unrolled iteration (if available)
        if i + 1 < len(equation):
            item = equation[i + 1]
            if item.isdigit():
                operand_stack.append(int(item))
            elif item in operators:
                operator_stack.append(item)

        # More heavy computation
        extra_computation = sum(random.randint(1, 1000000) for _ in range(1000))

# Example setup
equation = "3 + 5 * ( 2 - 8 )"
operand_stack = []
operator_stack = []
operators = {'+': lambda a, b: a + b, '*': lambda a, b: a * b}

unrolled_loop(equation, operand_stack, operator_stack, operators)

import sys
import time
from pyJoules.energy_meter import measure_energy
import random

@measure_energy
def early_termination_loop(equation, operand_stack, operator_stack, operators):
    for i in equation:
        if random.randint(0, 100) < 10:  # Example of early exit condition
            break
        if i.isdigit():
            operand_stack.append(int(i))
        elif i in operators:
            operator_stack.append(i)

        # Simulated additional computation
        large_computation = sum(random.randint(1, 1000000) for _ in range(1000))

# Example setup
equation = "3 + 5 * ( 2 - 8 )"
operand_stack = []
operator_stack = []
operators = {'+': lambda a, b: a + b, '*': lambda a, b: a * b}

early_termination_loop(equation, operand_stack, operator_stack, operators)

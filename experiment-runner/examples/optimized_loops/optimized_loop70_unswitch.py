import sys
import time
from pyJoules.energy_meter import measure_energy
import random

@measure_energy
def unswitched_loop(equation, operand_stack, operator_stack, operators):
    for i in equation:
        is_digit = i.isdigit()  # Move the check outside the loop
        if is_digit:
            operand_stack.append(int(i))
        elif i in operators:
            operator_stack.append(i)

        # Simulated additional computation
        large_computation = sum(random.randint(1, 1000000) ** 2 for _ in range(1000))

# Example setup
equation = "3 + 5 * ( 2 - 8 )"
operand_stack = []
operator_stack = []
operators = {'+': lambda a, b: a + b, '*': lambda a, b: a * b}

unswitched_loop(equation, operand_stack, operator_stack, operators)

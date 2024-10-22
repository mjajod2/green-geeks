import sys
import time
import random
from pyJoules.energy_meter import measure_energy

# Function to generate a long random expression
def generate_long_expression(length):
    operands = [str(random.randint(1, 100)) for _ in range(length)]
    operators = ['+', '*', '-', '/']
    expression = []
    for i in range(length):
        expression.append(operands[i])
        if i < length - 1:
            expression.append(random.choice(operators))
    return ' '.join(expression)

@measure_energy
def early_termination_loop(expression, stack, calc, is_operand):
    expression = expression.split()[::-1]
    for c in expression:
        if random.randint(0, 100) < 10:  # Early exit condition based on a 10% chance
            print("Early termination triggered")
            break
        if is_operand(c):
            stack.append(int(c))
        else:
            if len(stack) >= 2:
                o1 = stack.pop()
                o2 = stack.pop()
                stack.append(calc[c](o1, o2))
            else:
                print("Error: not enough operands in stack")
                return  # Exit if invalid operation

        # Heavy computation for energy consumption
        for _ in range(10000):  # Increase iterations to simulate more load
            large_computation = sum(random.randint(1, 1000000) ** 2 for _ in range(100))

# Example setup with a long expression
expression = generate_long_expression(10000)  # Generate an expression with 10,000 operands and operators
stack = []
calc = {'+': lambda o1, o2: o1 + o2, '*': lambda o1, o2: o1 * o2, '-': lambda o1, o2: o1 - o2, '/': lambda o1, o2: o1 / o2}
is_operand = lambda x: x.isdigit()

early_termination_loop(expression, stack, calc, is_operand)

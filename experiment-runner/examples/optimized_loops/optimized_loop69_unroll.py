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
def unrolled_loop(expression, stack, calc, is_operand):
    expression = expression.split()[::-1]
    for i in range(0, len(expression), 2):  # Unroll the loop to process two iterations at a time
        # First unrolled iteration
        c = expression[i]
        if is_operand(c):
            stack.append(int(c))
        else:
            if len(stack) >= 2:  # Ensure there are at least 2 operands to pop
                o1 = stack.pop()
                o2 = stack.pop()
                stack.append(calc[c](o1, o2))
            else:
                print("Error: not enough operands in stack for operation")
                return  # Terminate early if invalid operation

        # Heavy computation
        for _ in range(10000):  # Increase iterations to simulate more load
            large_computation = sum(random.randint(1, 1000000) ** 2 / (random.randint(1, 1000) + 1) for _ in range(100))

        # Second unrolled iteration (if exists)
        if i + 1 < len(expression):
            c = expression[i + 1]
            if is_operand(c):
                stack.append(int(c))
            else:
                if len(stack) >= 2:  # Ensure there are at least 2 operands to pop
                    o1 = stack.pop()
                    o2 = stack.pop()
                    stack.append(calc[c](o1, o2))
                else:
                    print("Error: not enough operands in stack for operation")
                    return  # Terminate early if invalid operation

        # Additional heavy computation
        for _ in range(10000):  # Increase iterations for more load
            extra_computation = sum(random.randint(1, 1000000) ** 2 for _ in range(100))

# Example setup with a long expression
expression = generate_long_expression(10000)  # Generate an expression with 10,000 operands and operators
stack = []
calc = {'+': lambda o1, o2: o1 + o2, '*': lambda o1, o2: o1 * o2, '-': lambda o1, o2: o1 - o2, '/': lambda o1, o2: o1 / o2}
is_operand = lambda x: x.isdigit()

unrolled_loop(expression, stack, calc, is_operand)

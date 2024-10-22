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
def unswitched_loop(expression, stack, calc, is_operand):
    expression = expression.split()[::-1]  # Reverse the expression list
    for c in expression:
        is_op = is_operand(c)  # Move the operand check outside the loop
        if is_op:
            stack.append(int(c))
        else:
            if len(stack) >= 2:  # Ensure there are at least two operands to pop
                o1 = stack.pop()
                o2 = stack.pop()
                stack.append(calc[c](o1, o2))
            else:
                print("Error: not enough operands in the stack for operation")
                return  # Exit early if there's an error

        # Perform intensive computations directly inside the loop
        for _ in range(1000):  # Outer loop for more iterations
            result = 0
            for i in range(1000):  # Inner loop with floating-point operations
                value = random.randint(1, 1000000)
                result += value ** 2 / (i + 1)

# Example setup
expression = generate_long_expression(10000)  # Generate an expression with 10,000 operands and operators
stack = []
calc = {'+': lambda o1, o2: o1 + o2, '*': lambda o1, o2: o1 * o2, '-': lambda o1, o2: o1 - o2, '/': lambda o1, o2: o1 / o2}
is_operand = lambda x: x.isdigit()

unswitched_loop(expression, stack, calc, is_operand)

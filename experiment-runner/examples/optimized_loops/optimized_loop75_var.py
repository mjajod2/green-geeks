import sys
import time
import random
from pyJoules.energy_meter import measure_energy

@measure_energy
def var_termination_loop(stack, post_fix, print_width):
    while len(stack) > 0:
        last_element = stack[-1]  # Cache stack[-1] outside the loop
        
        # Handle parentheses instead of raising an error
        if last_element == '(':
            post_fix.append(stack.pop())  # Just pop '(' and continue
        else:
            post_fix.append(stack.pop())

        # Heavy computation for energy consumption
        large_computation = sum(random.randint(1, 1000000) for _ in range(100))

        # Print statement for current stack and post_fix
        # print(' '.center(8), ''.join(stack).ljust(print_width), ''.join(post_fix).ljust(print_width), sep=' | ')

# Example setup
stack = ['+', '*', '(', ')'] * 1000  # Increase stack size for more iterations
post_fix = []
print_width = 8

var_termination_loop(stack, post_fix, print_width)

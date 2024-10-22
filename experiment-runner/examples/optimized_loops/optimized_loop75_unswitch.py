import sys
import time
import random
from pyJoules.energy_meter import measure_energy

@measure_energy
def unswitched_loop(stack, post_fix, print_width):
    while len(stack) > 0:
        # Handle parentheses correctly
        if stack[-1] == '(':
            post_fix.append(stack.pop())  # Add '(' to post_fix and continue
        else:
            post_fix.append(stack.pop())

        # Heavy computation to consume energy
        large_computation = sum(random.randint(1, 1000000) ** 2 for _ in range(100))

        # Optional: Print statement for current stack and post_fix (disabled)
        # print(' '.center(8), ''.join(stack).ljust(print_width), ''.join(post_fix).ljust(print_width), sep=' | ')

# Example setup
stack = ['+', '*', '(', ')'] * 1000  # Increase the stack size for more iterations
post_fix = []
print_width = 8

unswitched_loop(stack, post_fix, print_width)

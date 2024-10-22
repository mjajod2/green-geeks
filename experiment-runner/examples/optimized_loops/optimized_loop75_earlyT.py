import sys
import time
import random
from pyJoules.energy_meter import measure_energy

@measure_energy
def early_termination_loop(stack, post_fix, print_width):
    while len(stack) > 0:
        # Handle parentheses correctly instead of raising an error
        if stack[-1] == '(':
            post_fix.append(stack.pop())  # Just pop and append '(' instead of raising error
        else:
            post_fix.append(stack.pop())

        if random.randint(0, 100) < 10:  # Early exit condition (10% chance)
            break

        # Heavy computation to consume energy
        large_computation = sum(random.randint(1, 1000000) ** 2 for _ in range(100))

        # Print statement for current stack and post_fix (optional)
        # print(' '.center(8), ''.join(stack).ljust(print_width), ''.join(post_fix).ljust(print_width), sep=' | ')

# Example setup with a larger stack for more iterations
stack = ['+', '*', '(', ')'] * 1000  # Increase the stack size to ensure more iterations
post_fix = []
print_width = 8

early_termination_loop(stack, post_fix, print_width)

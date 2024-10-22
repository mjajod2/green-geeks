import sys
import time
import random
from pyJoules.energy_meter import measure_energy

@measure_energy
def unrolled_loop(stack, post_fix, print_width):
    while len(stack) > 0:
        # First unrolled iteration
        if stack[-1] == '(':
            # Handle parentheses properly, do not treat it as an error prematurely
            post_fix.append(stack.pop())  # Assuming '(' gets added to post_fix
        else:
            post_fix.append(stack.pop())
        
        # Heavy computation
        large_computation = sum(random.randint(1, 1000000) ** 2 for _ in range(100))

        # Print statement for current stack and post_fix
        # print(' '.center(8), ''.join(stack).ljust(print_width), ''.join(post_fix).ljust(print_width), sep=' | ')

        # Second unrolled iteration (if stack is not empty)
        if len(stack) > 0:
            if stack[-1] == '(':
                # Handle parentheses again without raising an error unnecessarily
                post_fix.append(stack.pop())  # Continue processing parentheses
            else:
                post_fix.append(stack.pop())

            # Additional heavy computation
            extra_computation = sum(random.randint(1, 1000000) for _ in range(100))

            # Print statement for current stack and post_fix
            # print(' '.center(8), ''.join(stack).ljust(print_width), ''.join(post_fix).ljust(print_width), sep=' | ')

# Example setup
stack = ['+', '*', '(', ')'] * 2500  # Make the stack large for more iterations
post_fix = []
print_width = 8

unrolled_loop(stack, post_fix, print_width)

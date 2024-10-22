import sys
import time
from pyJoules.energy_meter import measure_energy
import random

@measure_energy
def unswitched_loop(infix, post_fix, stack, priority, print_width):
    for x in infix:
        is_alpha_digit = x.isalpha() or x.isdigit()  # Move check outside the loop
        if is_alpha_digit:
            post_fix.append(x)
        elif x == '(':
            stack.append(x)
        elif x == ')':
            while stack and stack[-1] != '(':
                post_fix.append(stack.pop())
            stack.pop()

        # Simulated additional computation
        large_computation = sum(random.randint(1, 1000000) ** 2 for _ in range(1000))

# Example setup
infix = "(A+B)*C"
post_fix = []
stack = []
priority = {'+': 1, '*': 2}
print_width = 8

unswitched_loop(infix, post_fix, stack, priority, print_width)

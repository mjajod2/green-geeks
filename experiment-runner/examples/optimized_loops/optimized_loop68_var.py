import sys
import time
from pyJoules.energy_meter import measure_energy
import random

@measure_energy
def var_termination_loop(stack, arr, index):
    comparison_value = arr[index]  # Cache the termination condition
    while stack and stack[-1] <= comparison_value:
        stack.pop()
        if not stack:
            break

        # Additional heavy computation using cached value
        large_computation = sum(comparison_value ** 2 for _ in range(1000))

# Example setup
arr = [random.randint(1, 1000000) for _ in range(1000)]
stack = [random.randint(1, 1000000) for _ in range(10)]

var_termination_loop(stack, arr, 500)

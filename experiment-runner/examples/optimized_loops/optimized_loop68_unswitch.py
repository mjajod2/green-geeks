import sys
import time
import random
from pyJoules.energy_meter import measure_energy

@measure_energy
def unswitched_loop(stack, arr, index):
    comparison_value = arr[index]  # Move the comparison outside the loop
    while stack and stack[-1] <= comparison_value:
        stack.pop()
        if not stack:
            break

        # Simulate additional heavy computation with floating-point operations
        for _ in range(10000):  # Increase the number of iterations for more load
            extra_computation = sum(random.randint(1, 1000000) ** 2 / (random.randint(1, 1000) + 1) for _ in range(100))

# Example setup
arr = [random.randint(1, 1000000) for _ in range(100000)]  # Larger array to allow more work
stack = [random.randint(1, 1000000) for _ in range(1000)]  # Larger stack for more pops

unswitched_loop(stack, arr, 500)

import sys
import time
import random
from pyJoules.energy_meter import measure_energy

@measure_energy
def early_termination_loop(stack, arr, index):
    while stack and stack[-1] <= arr[index]:
        stack.pop()
        if not stack:
            break  # Early termination when stack is empty

        # Simulated additional heavy computation
        for _ in range(1000):  # Increase iterations to simulate more load
            large_computation = sum(random.randint(1, 1000000) ** 2 / (random.randint(1, 1000) + 1) for _ in range(100))

# Example setup
arr = [random.randint(1, 1000000) for _ in range(100000)]  # Increased array size to 100,000 elements
stack = [random.randint(1, 1000000) for _ in range(1000)]  # Increased stack size for more operations

early_termination_loop(stack, arr, 500)

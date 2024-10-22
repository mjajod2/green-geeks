import sys
import time
from pyJoules.energy_meter import measure_energy
import random

@measure_energy
def early_termination_computation_loop(arr, outer, i):
    for inner in arr[i + 1:]:
        large_computation = sum(random.randint(1, 1000000) for _ in range(1000))
        if outer < inner:
            next_item = large_computation
            break  # Exit early as soon as the condition is met

        # Additional heavy computation even after early exit is not met
        extra_computation = sum(random.randint(1, 1000000) ** 2 for _ in range(1000))

# Example setup
arr = [random.randint(1, 1000000) for _ in range(1000)]

early_termination_computation_loop(arr, 500, 0)

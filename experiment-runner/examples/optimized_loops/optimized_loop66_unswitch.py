import sys
import time
from pyJoules.energy_meter import measure_energy
import random

@measure_energy
def unswitched_computation_loop(arr, outer, i):
    func_result = random.randint(1, 1000000)  # Move constant operation outside the loop
    for inner in arr[i + 1:]:
        large_computation = sum(random.randint(1, 1000000) for _ in range(1000))
        if outer < inner:
            next_item = large_computation

        # Additional heavy computation
        extra_computation = sum(func_result ** 2 for _ in range(1000))  # Use the precomputed func_result for load

# Example setup
arr = [random.randint(1, 1000000) for _ in range(1000)]

unswitched_computation_loop(arr, 500, 0)

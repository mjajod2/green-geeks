import sys
import time
from pyJoules.energy_meter import measure_energy
import random

@measure_energy
def var_termination_computation_loop(arr, outer, i):
    next_item = random.randint(1, 1000000)  # Cache constant expression outside the loop
    for inner in arr[i + 1:]:
        large_computation = sum(random.randint(1, 1000000) for _ in range(1000))
        if outer < inner:
            next_item = large_computation

        # Additional heavy computation using the cached next_item value
        extra_computation = sum(next_item ** 2 for _ in range(1000))

# Example setup
arr = [random.randint(1, 1000000) for _ in range(1000)]

var_termination_computation_loop(arr, 500, 0)

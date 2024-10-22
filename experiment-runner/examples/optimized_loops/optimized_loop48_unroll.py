import sys
import time
from pyJoules.energy_meter import measure_energy
import random


@measure_energy
def extracted_loop_48():
    # Mocking left and right lists
    left = [random.randint(0, 1000) for _ in range(5_000_000)]
    right = [random.randint(0, 1000) for _ in range(5_000_000)]
    result = []
    while left and right:
        result.append(left.pop(0) if left[0] <= right[0] else right.pop(0))
        if left and right:  # Unroll second iteration
            result.append(left.pop(0) if left[0] <= right[0] else right.pop(0))

# Call the function
extracted_loop_48()
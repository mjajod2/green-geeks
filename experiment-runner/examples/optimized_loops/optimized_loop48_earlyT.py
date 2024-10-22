import sys
import time
from pyJoules.energy_meter import measure_energy
import random


@measure_energy
def extracted_loop_48():
    # Mocking left and right lists
    left = [random.randint(0, 1000) for _ in range(5000)]
    right = [random.randint(0, 1000) for _ in range(5000)]
    result = []
    while left and right:
        result.append(left.pop(0) if left[0] <= right[0] else right.pop(0))
        if len(result) >= len(left) // 2:  # Early termination condition
            break

# Call the function
extracted_loop_48()
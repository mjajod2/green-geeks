import sys
import time
from pyJoules.energy_meter import measure_energy
import random

# Mocking left and right lists
left = [random.randint(0, 1000) for _ in range(5_000_000)]
right = [random.randint(0, 1000) for _ in range(5_000_000)]
result = []

@measure_energy
def extracted_loop_48():
    while left and right:
        result.append(left.pop(0) if left[0] <= right[0] else right.pop(0))
        if len(result) >= len(left) // 2:  # Early termination condition
            break

# Call the function
extracted_loop_48()

# Display results
print(f'First few elements of result: {result[:10]}')

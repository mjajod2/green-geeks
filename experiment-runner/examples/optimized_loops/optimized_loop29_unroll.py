import sys
import time
from pyJoules.energy_meter import measure_energy
import random

# Mocking a large dataset with 10 million elements
array = [random.randint(0, 10) for _ in range(10_000_000)]
item = array[0]
pos = 0
cycle_start = 0
array_len = len(array)

@measure_energy
def extracted_loop_29():
    for i in range(cycle_start + 1, array_len, 4):  # unrolling by 4
        if i < array_len and array[i] < item:
            pos += 1
        if i+1 < array_len and array[i+1] < item:
            pos += 1
        if i+2 < array_len and array[i+2] < item:
            pos += 1
        if i+3 < array_len and array[i+3] < item:
            pos += 1

# Call the function
extracted_loop_29()

# Display the final position after the loop has run
print(f'Final position: {pos}')
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
def extracted_loop_28():
    while pos != cycle_start:
        pos = cycle_start
        for i in range(cycle_start + 1, array_len):
            if array[i] < item:
                pos += 1
        while item == array[pos]:
            pos += 1
        array[pos], item = (item, array[pos])
        if pos >= array_len:  # early termination condition
            break

# Call the function
extracted_loop_28()

# Display the final state after the loop has run
print(f'Final position: {pos}')

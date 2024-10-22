import sys
import time
from pyJoules.energy_meter import measure_energy
import random


@measure_energy
def extracted_loop_29():
    # Mocking a large dataset with 10 million elements
    array = [random.randint(0, 10) for _ in range(10_000_000)]
    item = array[0]
    pos = 0
    cycle_start = 0
    array_len = len(array)
    for i in range(cycle_start + 1, array_len):
        if array[i] < item:
            pos += 1
        if pos >= array_len // 2:  # Early termination condition
            break

# Call the function
extracted_loop_29()
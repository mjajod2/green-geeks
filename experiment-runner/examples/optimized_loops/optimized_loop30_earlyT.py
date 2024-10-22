import sys
import time
from pyJoules.energy_meter import measure_energy
import random

@measure_energy
def extracted_loop_30():
    # Mocking a large dataset with 10 million elements
    array = [random.randint(0, 10) for _ in range(10_000_000)]
    item = array[0]
    pos = 0
    while item == array[pos]:
        pos += 1
        if pos >= len(array):  # Early termination condition
            break

# Call the function
extracted_loop_30()
import sys
import time
from pyJoules.energy_meter import measure_energy
import random


@measure_energy
def extracted_loop_47():
    # Mocking a list of integers with 10 million elements
    list_of_ints = [random.randint(0, 1000) for _ in range(10_000_000)]
    bit_position = 4  # Example bit position
    i, j = 0, len(list_of_ints) - 1  # Initial indices
    while i <= j:
        changed = False
        if not list_of_ints[i] >> bit_position & 1:
            i += 1
            changed = True
        if list_of_ints[j] >> bit_position & 1:
            j -= 1
            changed = True
        if changed:
            continue
        list_of_ints[i], list_of_ints[j] = (list_of_ints[j], list_of_ints[i])
        j -= 1
        if j != i:
            i += 1
        if i <= j and not list_of_ints[i] >> bit_position & 1:  # Unrolling second iteration
            i += 1
            changed = True

# Call the function
extracted_loop_47()
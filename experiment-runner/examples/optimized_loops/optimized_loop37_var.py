import sys
import time
from pyJoules.energy_meter import measure_energy
import random


@measure_energy
def extracted_loop_37():
    # Mocking a sorting array with 10 million elements
    sorting = [random.randint(0, 100) for _ in range(10_000_000)]
    pivot = sorting[len(sorting) // 2]  # Example pivot element
    store_index = 0
    left = 0
    right = len(sorting)
    max_right = right  # Variable for loop termination
    for i in range(left, max_right):
        if sorting[i] < pivot:
            sorting[store_index], sorting[i] = (sorting[i], sorting[store_index])
            store_index += 1

# Call the function
extracted_loop_37()

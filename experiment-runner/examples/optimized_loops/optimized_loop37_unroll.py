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
    for i in range(left, right, 2):  # Unrolling by 2
        if sorting[i] < pivot:
            sorting[store_index], sorting[i] = (sorting[i], sorting[store_index])
            store_index += 1
        if i + 1 < right and sorting[i + 1] < pivot:
            sorting[store_index], sorting[i + 1] = (sorting[i + 1], sorting[store_index])
            store_index += 1

# Call the function
extracted_loop_37()

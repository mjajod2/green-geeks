import sys
import time
from pyJoules.energy_meter import measure_energy
import random


@measure_energy
def extracted_loop_36():
    # Mocking a sorting array with 10 million elements
    sorting = [random.randint(0, 100) for _ in range(10_000_000)]
    pivot = sorting[len(sorting) // 2]  # Example pivot element
    a = 0
    b = len(sorting) - 1
    i = 0
    while i <= b:
        if sorting[i] < pivot:
            sorting[a], sorting[i] = (sorting[i], sorting[a])
            a += 1
            i += 1
        elif sorting[i] > pivot:
            sorting[b], sorting[i] = (sorting[i], sorting[b])
            b -= 1
        else:
            i += 1
        if i <= b and sorting[i] < pivot:  # Unrolling second iteration
            sorting[a], sorting[i] = (sorting[i], sorting[a])
            a += 1
            i += 1

# Call the function
extracted_loop_36()
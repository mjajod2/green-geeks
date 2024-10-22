import sys
import time
from pyJoules.energy_meter import measure_energy
import random

# Mocking a sorting array with 10 million elements
sorting = [random.randint(0, 100) for _ in range(10_000_000)]
pivot = sorting[len(sorting) // 2]  # Example pivot element
a = 0
b = len(sorting) - 1
i = 0

@measure_energy
def extracted_loop_36():
    max_i = len(sorting)  # Variable for loop termination
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
        if i >= max_i // 2:  # Early termination using a variable
            break

# Call the function
extracted_loop_36()

# Display a portion of the sorted array after the loop has run
print(f'First few elements: {sorting[:10]}')
import sys
import time
from pyJoules.energy_meter import measure_energy
import random


@measure_energy
def extracted_loop_40():
    # Mocking a collection with 10 million elements
    collection = [random.randint(0, 100) for _ in range(10_000_000)]
    gap = len(collection) // 2  # Example gap
    j = len(collection) - 1  # Example starting point
    temp = collection[j]
    while j >= gap and collection[j - gap] > temp:
        collection[j] = collection[j - gap]
        j -= gap
        if j >= gap and collection[j - gap] > temp:  # Unrolling second iteration
            collection[j] = collection[j - gap]
            j -= gap

# Call the function
extracted_loop_40()

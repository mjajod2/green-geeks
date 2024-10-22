import sys
import time
from pyJoules.energy_meter import measure_energy
import random


@measure_energy
def extracted_loop_38():
    # Mocking a collection with 10 million elements
    collection = [random.randint(0, 100) for _ in range(10000)]
    gap = len(collection) // 2  # Initial gap for shell sort
    shrink = 1.3  # Example shrink factor for gap reduction
    min_gap = len(collection) // 10  # Variable for loop termination
    while gap > 1:
        gap = int(gap / shrink)
        for i in range(gap, len(collection)):
            temp = collection[i]
            j = i
            while j >= gap and collection[j - gap] > temp:
                collection[j] = collection[j - gap]
                j -= gap
            collection[j] = temp
        if gap <= min_gap:
            break

# Call the function
extracted_loop_38()

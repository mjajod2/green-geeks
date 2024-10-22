import sys
import time
from pyJoules.energy_meter import measure_energy
import random


@measure_energy
def extracted_loop_39():
    # Mocking a collection with 10 million elements
    collection = [random.randint(0, 100) for _ in range(10_000_000)]
    gap = len(collection) // 2  # Example gap
    max_i = len(collection)  # Variable for loop termination
    for i in range(gap, max_i):
        temp = collection[i]
        j = i
        while j >= gap and collection[j - gap] > temp:
            collection[j] = collection[j - gap]
            j -= gap
        collection[j] = temp

# Call the function
extracted_loop_39()

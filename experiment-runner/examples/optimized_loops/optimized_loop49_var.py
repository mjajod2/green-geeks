import sys
import time
from pyJoules.energy_meter import measure_energy
import random


@measure_energy
def extracted_loop_49():
    # Mocking a collection with 10 million elements
    collection = [random.randint(0, 1000) for _ in range(10000)]
    n = len(collection)
    max_iters = n // 2  # Variable for loop termination
    for i in range(1, max_iters):
        value_to_insert = collection[i]
        low = 0
        high = i - 1
        while low <= high:
            mid = (low + high) // 2
            if value_to_insert < collection[mid]:
                high = mid - 1
            else:
                low = mid + 1
        for j in range(i, low, -1):
            collection[j] = collection[j - 1]
        collection[low] = value_to_insert

# Call the function
extracted_loop_49()
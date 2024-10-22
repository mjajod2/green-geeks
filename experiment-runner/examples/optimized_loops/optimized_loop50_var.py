import sys
import time
from pyJoules.energy_meter import measure_energy
import random


@measure_energy
def extracted_loop_50():
    # Mocking a collection and variables
    collection = [random.randint(0, 1000) for _ in range(10_000_000)]
    value_to_insert = collection[len(collection) // 2]  # Example value
    low = 0
    high = len(collection) - 1
    max_iters = len(collection) // 2  # Variable for loop termination
    for _ in range(max_iters):  # Control loop by variable
        if low > high:
            break
        mid = (low + high) // 2
        if value_to_insert < collection[mid]:
            high = mid - 1
        else:
            low = mid + 1

# Call the function
extracted_loop_50()
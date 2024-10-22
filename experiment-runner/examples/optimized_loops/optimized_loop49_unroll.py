import sys
import time
from pyJoules.energy_meter import measure_energy
import random

# Mocking a collection with 10 million elements
collection = [random.randint(0, 1000) for _ in range(10_000_000)]
n = len(collection)

@measure_energy
def extracted_loop_49():
    for i in range(1, n):
        value_to_insert = collection[i]
        low = 0
        high = i - 1
        while low <= high:
            mid = (low + high) // 2
            if value_to_insert < collection[mid]:
                high = mid - 1
            else:
                low = mid + 1
        for j in range(i, low, -2):  # Unrolling by processing two elements at once
            collection[j] = collection[j - 1]
            if j - 1 > low:
                collection[j - 1] = collection[j - 2]
        collection[low] = value_to_insert

# Call the function
extracted_loop_49()

# Display results
print(f'First few elements of the sorted collection: {collection[:10]}')

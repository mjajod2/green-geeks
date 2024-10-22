import sys
import time
from pyJoules.energy_meter import measure_energy
import random

# Mocking a collection and variables
collection = [random.randint(0, 1000) for _ in range(10_000_000)]
value_to_insert = collection[len(collection) // 2]  # Example value
low = 0
high = len(collection) - 1

@measure_energy
def extracted_loop_50():
    while low <= high:
        mid = (low + high) // 2
        if value_to_insert < collection[mid]:
            high = mid - 1
        else:
            low = mid + 1
        if low <= high:  # Unroll second iteration
            mid = (low + high) // 2
            if value_to_insert < collection[mid]:
                high = mid - 1
            else:
                low = mid + 1

# Call the function
extracted_loop_50()

# Display final low and high values
print(f'Low: {low}, High: {high}')

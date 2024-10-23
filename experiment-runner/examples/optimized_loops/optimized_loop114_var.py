import sys
import time
from pyJoules.energy_meter import measure_energy
import random

# Mocking a collection and variables
collection = [random.randint(0, 1000) for _ in range(10_000_000)]
left = 0
right = len(collection) - 1
swapped = False
max_iters = len(collection) // 2  # Variable for loop termination

@measure_energy
def extracted_loop_114():
    for _ in range(max_iters):
        if left >= right:
            break
        if collection[left] > collection[right]:
            collection[left], collection[right] = (collection[right], collection[left])
            swapped = True
        left += 1
        right -= 1

# Call the function
extracted_loop_114()

# Display final results (first 10 elements of the collection)
print(f'First few elements of the collection: {collection[:10]}')
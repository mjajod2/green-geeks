import sys
import time
from pyJoules.energy_meter import measure_energy
import random

# Mocking a large dataset with 10 million elements
array = [random.randint(0, 10) for _ in range(10_000_000)]
item = array[0]  # Assume the first element is the item we want to match
pos = 0

@measure_energy
def extracted_loop_27():
    while item == array[pos]:
        pos += 1
        if pos >= len(array):  # early termination when out of bounds
            break

# Call the function
extracted_loop_27()

# Display the final position after the loop has run
print(f'Final position: {pos}')

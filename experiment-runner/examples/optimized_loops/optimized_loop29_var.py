import sys
import time
from pyJoules.energy_meter import measure_energy
import random

# Mocking a large dataset with 10 million elements
array = [random.randint(0, 10) for _ in range(10_000_000)]
item = array[0]
pos = 0
max_pos = len(array)  # Using a variable for loop termination

@measure_energy
def extracted_loop_30():
    while pos < max_pos and item == array[pos]:
        pos += 1

# Call the function
extracted_loop_30()

# Display the final position after the loop has run
print(f'Final position: {pos}')
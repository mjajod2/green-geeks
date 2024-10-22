import sys
import time
from pyJoules.energy_meter import measure_energy
import random

# Mocking a large dataset with 10 million elements
array = [random.randint(0, 10) for _ in range(10_000_000)]
item = array[0]
pos = 0

@measure_energy
def extracted_loop_30():
    if item >= array[0]:  # Assuming a precondition
        while item == array[pos]:
            pos += 1
    else:
        return  # Skip loop if precondition is false

# Call the function
extracted_loop_30()

# Display the final position after the loop has run
print(f'Final position: {pos}')

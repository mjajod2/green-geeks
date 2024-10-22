import sys
import time
from pyJoules.energy_meter import measure_energy
import random

# Mocking a list of integers with 10 million elements
list_of_ints = [random.randint(0, 1000) for _ in range(10_000_000)]
bit_position = 4  # Example bit position
ones = []
zeros = []
max_iters = len(list_of_ints) // 2  # Variable for loop termination

@measure_energy
def extracted_loop_46():
    for i, number in enumerate(list_of_ints[:max_iters]):
        if number >> bit_position - 1 & 1:
            ones.append(number)
        else:
            zeros.append(number)

# Call the function
extracted_loop_46()

# Display results
print(f'First few ones: {ones[:10]}')
print(f'First few zeros: {zeros[:10]}')
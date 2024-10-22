import sys
import time
from pyJoules.energy_meter import measure_energy
import random

# Mocking a sequence with 10 million elements
sequence = [random.randint(0, 100) for _ in range(10_000_000)]

@measure_energy
def extracted_loop_45():
    for i, (rod_upper, rod_lower) in enumerate(zip(sequence, sequence[1:])):
        if rod_upper > rod_lower:
            sequence[i] -= rod_upper - rod_lower
            sequence[i + 1] += rod_upper - rod_lower
        if i >= len(sequence) // 2:  # Early termination condition
            break

# Call the function
extracted_loop_45()

# Display a portion of the sequence after the loop has run
print(f'First few elements: {sequence[:10]}')

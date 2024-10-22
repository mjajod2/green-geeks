import sys
import time
from pyJoules.energy_meter import measure_energy
import random

# Mocking a sequence with 10 million elements
sequence = [random.randint(0, 100) for _ in range(10_000_000)]

@measure_energy
def extracted_loop_45():
    for i in range(0, len(sequence) - 1, 2):  # Unrolling by processing two pairs
        rod_upper, rod_lower = sequence[i], sequence[i + 1]
        if rod_upper > rod_lower:
            sequence[i] -= rod_upper - rod_lower
            sequence[i + 1] += rod_upper - rod_lower
        if i + 2 < len(sequence) - 1:  # Handle the next pair in unrolling
            rod_upper_next, rod_lower_next = sequence[i + 1], sequence[i + 2]
            if rod_upper_next > rod_lower_next:
                sequence[i + 1] -= rod_upper_next - rod_lower_next
                sequence[i + 2] += rod_upper_next - rod_lower_next

# Call the function
extracted_loop_45()

# Display a portion of the sequence after the loop has run
print(f'First few elements: {sequence[:10]}')
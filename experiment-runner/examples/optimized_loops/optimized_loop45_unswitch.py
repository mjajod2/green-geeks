import sys
import time
from pyJoules.energy_meter import measure_energy
import random

@measure_energy
def extracted_loop_45():
    # Mocking a sequence with 10 million elements
    sequence = [random.randint(0, 100) for _ in range(10_000_000)]
    if len(sequence) > 1:  # Precondition to check sequence length
        for i, (rod_upper, rod_lower) in enumerate(zip(sequence, sequence[1:])):
            if rod_upper > rod_lower:
                sequence[i] -= rod_upper - rod_lower
                sequence[i + 1] += rod_upper - rod_lower

# Call the function
extracted_loop_45()
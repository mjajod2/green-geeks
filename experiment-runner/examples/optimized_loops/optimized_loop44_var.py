import sys
import time
from pyJoules.energy_meter import measure_energy
import random


@measure_energy
def extracted_loop_44():
    # Mocking a sequence with 10 million elements
    sequence = [random.randint(0, 100) for _ in range(10_000_000)]
    max_iters = len(sequence) // 2  # Variable for loop termination
    for _ in range(max_iters):
        for i, (rod_upper, rod_lower) in enumerate(zip(sequence, sequence[1:])):
            if rod_upper > rod_lower:
                sequence[i] -= rod_upper - rod_lower
                sequence[i + 1] += rod_upper - rod_lower

# Call the function
extracted_loop_44()
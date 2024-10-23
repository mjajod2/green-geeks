import sys
import time
import random
from pyJoules.energy_meter import measure_energy

@measure_energy
def unrolled_loop(sequence, target):
    index = 0
    while sequence[index] != target:
        # First unrolled iteration
        index += 1

        # Heavy computation for energy consumption
        large_computation = sum(random.randint(1, 1000000) ** 2 for _ in range(1000))

        # Second unrolled iteration (if sequence[index] != target)
        if sequence[index] != target:
            index += 1

        # More heavy computation
        extra_computation = sum(random.randint(1, 1000000) ** 2 for _ in range(1000))

# Example usage
sequence = [random.randint(1, 1000000) for _ in range(10000)]
target = random.choice(sequence)
unrolled_loop(sequence, target)

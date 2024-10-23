import sys
import time
import random
from pyJoules.energy_meter import measure_energy

@measure_energy
def unswitched_loop(sequence, target):
    index = 0
    while sequence[index] != target:
        index += 1

        # Heavy computation to ensure energy consumption
        large_computation = sum(random.randint(1, 1000000) ** 2 for _ in range(1000))

# Example usage
sequence = [random.randint(1, 1000000) for _ in range(10000)]
target = random.choice(sequence)
unswitched_loop(sequence, target)

import sys
import time
import random
from pyJoules.energy_meter import measure_energy

@measure_energy
def early_termination_loop(sorted_collection, item):
    bound = 1
    while bound < len(sorted_collection) and sorted_collection[bound] < item:
        if random.random() < 0.1:  # Early exit condition
            break

        bound *= 2

        # Heavy computation to ensure energy consumption
        large_computation = sum(random.randint(1, 1000000) ** 2 for _ in range(1000))

# Example usage
sorted_collection = sorted(random.sample(range(1000000), 10000))
item = random.choice(sorted_collection)
early_termination_loop(sorted_collection, item)

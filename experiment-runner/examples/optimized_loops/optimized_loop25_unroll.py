import sys
import time
import random
from pyJoules.energy_meter import measure_energy

@measure_energy
def unrolled_loop(sorted_collection, item):
    bound = 1
    while bound < len(sorted_collection) and sorted_collection[bound] < item:
        # First unrolled iteration
        bound *= 2

        # Heavy computation to ensure energy consumption
        large_computation = sum(random.randint(1, 1000000) ** 2 for _ in range(1000))

        # Second unrolled iteration (if bound is still valid)
        if bound < len(sorted_collection) and sorted_collection[bound] < item:
            bound *= 2

        # More heavy computation
        extra_computation = sum(random.randint(1, 1000000) ** 2 for _ in range(1000))

# Example usage
sorted_collection = sorted(random.sample(range(1000000), 10000))
item = random.choice(sorted_collection)
unrolled_loop(sorted_collection, item)

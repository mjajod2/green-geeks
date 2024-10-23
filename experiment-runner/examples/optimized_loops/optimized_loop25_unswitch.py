import sys
import time
import random
from pyJoules.energy_meter import measure_energy

@measure_energy
def unswitched_loop(sorted_collection, item):
    bound = 1
    collection_len = len(sorted_collection)

    # Move boundary check outside the loop
    while bound < collection_len and sorted_collection[bound] < item:
        bound *= 2

        # Heavy computation for energy consumption
        large_computation = sum(random.randint(1, 1000000) ** 2 for _ in range(1000))

# Example usage
sorted_collection = sorted(random.sample(range(1000000), 10000))
item = random.choice(sorted_collection)
unswitched_loop(sorted_collection, item)
import sys
import time
import random
from pyJoules.energy_meter import measure_energy

@measure_energy
def var_termination_loop(sorted_collection, item, lo, hi):
    cached_hi = hi

    while lo < cached_hi:
        mid = lo + (cached_hi - lo) // 2
        if sorted_collection[mid] < item:
            lo = mid + 1
        else:
            cached_hi = mid

        # Heavy computation to ensure energy consumption
        large_computation = sum(random.randint(1, 1000000) ** 2 for _ in range(1000))

# Example usage
sorted_collection = sorted(random.sample(range(1000000), 10000))
item = random.choice(sorted_collection)
var_termination_loop(sorted_collection, item, 0, len(sorted_collection) - 1)

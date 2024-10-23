import sys
import time
import random
from pyJoules.energy_meter import measure_energy

@measure_energy
def unrolled_loop(sorted_collection, item, lo, hi):
    while lo < hi:
        # First unrolled iteration
        mid = lo + (hi - lo) // 2
        if sorted_collection[mid] < item:
            lo = mid + 1
        else:
            hi = mid

        # Heavy computation for energy consumption
        large_computation = sum(random.randint(1, 1000000) ** 2 for _ in range(1000))

        # Second unrolled iteration
        if lo < hi:
            mid = lo + (hi - lo) // 2
            if sorted_collection[mid] < item:
                lo = mid + 1
            else:
                hi = mid

        # More heavy computation
        extra_computation = sum(random.randint(1, 1000000) ** 2 for _ in range(1000))

# Example usage
sorted_collection = sorted(random.sample(range(1000000), 100000))
unrolled_loop(sorted_collection, 500000, 0, len(sorted_collection))

import sys
import time
import random
from pyJoules.energy_meter import measure_energy

@measure_energy
def early_termination_loop(sorted_collection, item, left, right):
    while left <= right:
        if random.random() < 0.1:  # Early exit condition
            break

        midpoint = left + (right - left) // 2
        current_item = sorted_collection[midpoint]
        
        if current_item == item:
            return midpoint
        elif item < current_item:
            right = midpoint - 1
        else:
            left = midpoint + 1

        # Heavy computation to ensure energy consumption
        large_computation = sum(random.randint(1, 1000000) ** 2 for _ in range(1000))

# Example usage
sorted_collection = sorted(random.sample(range(1000000), 10000))
item = random.choice(sorted_collection)
early_termination_loop(sorted_collection, item, 0, len(sorted_collection) - 1)

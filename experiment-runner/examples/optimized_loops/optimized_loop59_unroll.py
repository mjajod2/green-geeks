import sys
import time
from pyJoules.energy_meter import measure_energy
import random

@measure_energy
def unrolled_loop(sets, node):
    for i in range(0, len(sets), 2):  # Unroll the loop by processing two sets per iteration
        # First unrolled iteration
        if node.data in sets[i]:
            return sets[i]
        
        # Simulated computational work
        for _ in range(100):  # Simulate load to increase energy consumption
            random.randint(1, 1000000)

        # Second unrolled iteration (process another set in the same loop pass)
        if i + 1 < len(sets) and node.data in sets[i + 1]:
            return sets[i + 1]

        # Simulated computational work
        for _ in range(100):  # Simulate load to increase energy consumption
            random.randint(1, 1000000)

    return None

# Example setup
node = type("Node", (object,), {"data": random.randint(1, 1000000)})()
sets = [set(random.sample(range(1000000), 100)) for _ in range(1000)]  # 1 million sets with 100 elements

unrolled_loop(sets, node)

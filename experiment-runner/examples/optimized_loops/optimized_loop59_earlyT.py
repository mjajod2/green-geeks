import sys
import time
from pyJoules.energy_meter import measure_energy
import random

@measure_energy
def early_termination_loop(sets, node):
    for s in sets:
        if node.data in s:
            return s  # Early termination if node.data is found

        # Simulated computational work
        for _ in range(100):  # Simulate load to increase energy consumption
            random.randint(1, 1000000)

    return None

# Example setup
node = type("Node", (object,), {"data": random.randint(1, 1000000)})()
sets = [set(random.sample(range(1000000), 100)) for _ in range(1000)]  # 1 million sets with 100 elements

early_termination_loop(sets, node)

import sys
import time
from pyJoules.energy_meter import measure_energy
import random

@measure_energy
def var_termination_loop(sets, node):
    node_data = node.data  # Cache the termination condition
    for s in sets:
        if node_data in s:
            return s
        
        # Simulated computational work
        for _ in range(100):  # Simulate load to increase energy consumption
            random.randint(1, 1000000)

    return None

# Example setup
node = type("Node", (object,), {"data": random.randint(1, 1000000)})()
sets = [set(random.sample(range(1000000), 100)) for _ in range(1000)]  # 1 million sets with 100 elements

var_termination_loop(sets, node)

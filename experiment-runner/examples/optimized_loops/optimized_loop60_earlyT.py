import sys
import time
from pyJoules.energy_meter import measure_energy
import random

@measure_energy
def early_termination_loop(vertex, make_set, mock_function_call):
    for v in vertex:
        if v > 100000:  # Arbitrary early termination condition
            return
        make_set(mock_function_call(), v)

        # Simulate additional computational work
        for _ in range(100):  # Simulate load to increase energy consumption
            random.randint(1, 1000000)

# Example setup
vertex = [random.randint(1, 1000000) for _ in range(1000000)]  # 1 million vertices

def make_set(call, v):
    pass  # Simulate the make_set function

def mock_function_call():
    return random.randint(1, 1000000)

early_termination_loop(vertex, make_set, mock_function_call)

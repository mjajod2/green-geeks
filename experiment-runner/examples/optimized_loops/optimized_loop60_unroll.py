import sys
import time
from pyJoules.energy_meter import measure_energy
import random

@measure_energy
def unrolled_loop(vertex, make_set, mock_function_call):
    for i in range(0, len(vertex), 2):
        # First unrolled iteration
        make_set(mock_function_call(), vertex[i])

        # Simulate additional computational work
        for _ in range(100):  # Simulate load to increase energy consumption
            random.randint(1, 1000000)

        # Second unrolled iteration
        if i + 1 < len(vertex):
            make_set(mock_function_call(), vertex[i + 1])

        # Simulate additional computational work
        for _ in range(100):  # Simulate load to increase energy consumption
            random.randint(1, 1000000)

# Example setup
vertex = [random.randint(1, 1000000) for _ in range(10000)]  # 1 million vertices

def make_set(call, v):
    pass  # Simulate the make_set function

def mock_function_call():
    return random.randint(1, 1000000)

unrolled_loop(vertex, make_set, mock_function_call)

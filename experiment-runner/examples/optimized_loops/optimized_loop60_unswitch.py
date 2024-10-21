import sys
import time
from pyJoules.energy_meter import measure_energy
import random

@measure_energy
def unswitched_loop(vertex, make_set, mock_function_call):
    func_result = mock_function_call()  # Cache the mock_function_call result if constant
    for v in vertex:
        make_set(func_result, v)
        
        # Simulate additional computational work
        for _ in range(100):  # Simulate load to increase energy consumption
            random.randint(1, 1000000)

# Example setup
vertex = [random.randint(1, 1000000) for _ in range(10000)]  # 1 million vertices

def make_set(call, v):
    pass  # Simulate the make_set function

def mock_function_call():
    return random.randint(1, 1000000)

unswitched_loop(vertex, make_set, mock_function_call)

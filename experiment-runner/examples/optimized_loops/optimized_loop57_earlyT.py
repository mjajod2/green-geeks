import sys
import time
import random
from pyJoules.energy_meter import measure_energy

@measure_energy
def early_termination_loop(mock_function_call, mock_variable_assignment, arr, item, block_size):
    arr_size = len(arr)
    step = block_size
    prev = 0

    while arr[min(mock_function_call(), step, arr_size) - 1] < item:
        prev = step
        step += block_size
        if prev >= arr_size:
            return -1  # Early termination if 'prev' exceeds 'arr_size'

        # Simulate additional computational work with higher load
        for _ in range(100000):  # Increase loop iterations for more load
            val = mock_function_call()
            result = 0
            for i in range(100):  # Add floating-point operations for higher energy usage
                result += val * (i ** 2) / (i + 1)

    return prev  # Return the last value of 'prev'

# Example functions
def mock_function_call():
    return random.randint(1, 1000000)

def mock_variable_assignment():
    return random.randint(1, 1000000)

# Large dataset of 10 million elements
arr = random.sample(range(100000000), 10000000)  # 10 million elements
item = random.choice(arr)
block_size = 1000

early_termination_loop(mock_function_call, mock_variable_assignment, arr, item, block_size)

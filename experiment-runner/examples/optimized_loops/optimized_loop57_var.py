import sys
import time
from pyJoules.energy_meter import measure_energy
import random

@measure_energy
def var_termination_loop(mock_function_call, mock_variable_assignment, arr, item, block_size):
    arr_size = len(arr)  # Cache arr_size outside the loop
    step = block_size
    prev = 0

    while arr[min(mock_function_call(), step, arr_size) - 1] < item:
        prev = step
        step += block_size
        if prev >= arr_size:
            return -1  # Early return if 'prev' exceeds 'arr_size'

        # Simulate additional computational work
        for _ in range(100):  # Simulate load for energy measurement
            mock_function_call()

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

var_termination_loop(mock_function_call, mock_variable_assignment, arr, item, block_size)

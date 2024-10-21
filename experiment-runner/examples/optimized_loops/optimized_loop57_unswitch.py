import sys
import time
import random
from pyJoules.energy_meter import measure_energy

@measure_energy
def unswitched_loop(mock_function_call, mock_variable_assignment, arr, item, block_size):
    arr_size = len(arr)  # Cache the array size outside the loop
    step = block_size
    prev = 0

    while arr[min(mock_function_call(), step, arr_size) - 1] < item:
        prev = step
        step += block_size
        if prev >= arr_size:
            return -1

        # Simulate additional computational work
        for _ in range(100000):  # Increase the loop iteration to simulate more work
            # Intensive computation
            val = mock_function_call()
            result = 0
            for i in range(100):  # More complex nested loop
                result += val * (i ** 2) / (i + 1)  # Example of floating-point operations

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

unswitched_loop(mock_function_call, mock_variable_assignment, arr, item, block_size)

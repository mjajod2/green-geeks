import sys
import time
import random
from pyJoules.energy_meter import measure_energy

@measure_energy
def unrolled_loop(mock_function_call, mock_variable_assignment, arr, item, block_size):
    arr_size = len(arr)
    step = block_size
    prev = 0

    while True:
        # First unrolled iteration
        if arr[min(mock_function_call(), step, arr_size) - 1] < item:
            prev = step
            step += block_size
            if prev >= arr_size:
                return -1

        # Simulate additional computational work
        for _ in range(100000):  # Increase the iteration to consume more energy
            val = mock_function_call()
            result = 0
            for i in range(100):  # Add more intensive floating-point calculations
                result += val * (i ** 2) / (i + 1)

        # Second unrolled iteration
        if step >= arr_size or arr[min(mock_function_call(), step, arr_size) - 1] >= item:
            break  # Terminate if step exceeds array size or item is found

        # Simulate additional computational work
        for _ in range(100000):  # Increase load in the second iteration as well
            val = mock_function_call()
            result = 0
            for i in range(100):  # Add more intensive floating-point calculations
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

unrolled_loop(mock_function_call, mock_variable_assignment, arr, item, block_size)

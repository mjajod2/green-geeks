import sys
import time
import random
from pyJoules.energy_meter import measure_energy

@measure_energy
def unswitched_loop(arr, mock_function_call, mock_variable_assignment, i, arr_size):
    j = mock_function_call()  # Cache the result of the mock function call
    while j < arr_size:
        if arr[i] < arr[j]:
            next_element = arr[j]

            # Add computational work to consume more energy
            for _ in range(10000):  # Increase iterations to simulate load
                val = mock_function_call()
                result = 0
                for k in range(100):  # Complex floating-point operations
                    result += val * (k ** 2) / (k + 1)
            break
        j += 1

# Example setup
arr = [random.randint(1, 1000000) for _ in range(100000)]  # Array with 100,000 elements

def mock_function_call():
    return random.randint(1, 100000)

def mock_variable_assignment():
    return random.randint(1, 100000)

unswitched_loop(arr, mock_function_call, mock_variable_assignment, 0, len(arr))

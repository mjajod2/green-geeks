import sys
import time
import random
from pyJoules.energy_meter import measure_energy

@measure_energy
def early_termination_loop(arr, mock_function_call, mock_variable_assignment, i, arr_size):
    j = mock_function_call()
    while j < arr_size:
        if arr[i] < arr[j]:
            next_element = arr[j]

            # Simulate more computational work even with early termination
            for _ in range(10000):  # Add more iterations to consume energy
                val = mock_function_call()
                result = 0
                for k in range(100):  # Add floating-point calculations
                    result += val * (k ** 2) / (k + 1)

            break  # Early termination when the first condition is met
        j += 1

# Example setup
arr = [random.randint(1, 1000000) for _ in range(100000)]  # Increased array size to 100,000 elements

def mock_function_call():
    return random.randint(1, 100000)

def mock_variable_assignment():
    return random.randint(1, 100000)

early_termination_loop(arr, mock_function_call, mock_variable_assignment, 0, len(arr))

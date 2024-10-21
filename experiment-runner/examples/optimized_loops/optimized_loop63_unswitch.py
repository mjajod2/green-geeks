import sys
import time
from pyJoules.energy_meter import measure_energy
import random

@measure_energy
def unswitched_loop(arr, result, mock_function_call, mock_variable_assignment, arr_size):
    func_result = mock_function_call()  # Cache mock_function_call result outside inner loop
    for i in range(arr_size):
        next_element: float = mock_variable_assignment()
        for j in range(i + 1, arr_size):
            if arr[i] < arr[j]:
                next_element = arr[j]
                break
        result.append(func_result)

        # Simulate additional computational work
        for _ in range(100):  # Simulate load to increase energy consumption
            random.randint(1, 1000000)

# Example setup
arr = [random.randint(1, 1000000) for _ in range(1000)]  # Reduced to 1000 for performance
result = []

def mock_function_call():
    return random.randint(1, 100)

def mock_variable_assignment():
    return random.randint(1, 100)

unswitched_loop(arr, result, mock_function_call, mock_variable_assignment, len(arr))

import sys
import time
from pyJoules.energy_meter import measure_energy

# Mocking necessary variables
n = 10_000_000  # Dataset of 10 million items
arr = [i for i in range(n)]  # Mock array of 10 million items

def mock_function_call():
    return ''  # Return empty string for consistency in printing

def mock_variable_assignment():
    return ' '  # Mock variable assignment for end

mock_range = range

@measure_energy
def mock_loop_unroll():
    step = 4
    i = 0

    while i < n - step:
        for _ in range(step):
            # print(mock_function_call(), arr[i], end=mock_variable_assignment())
            i += 1

    # Handle remaining iterations
    while i < n:
        # print(mock_function_call(), arr[i], end=mock_variable_assignment())
        i += 1

# Call the function
mock_loop_unroll()
